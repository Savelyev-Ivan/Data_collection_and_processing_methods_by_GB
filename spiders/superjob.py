import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class SuperjobSpider(scrapy.Spider):
    name = 'superjob'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://russia.superjob.ru/vacancy/search/?keywords=python']

    def parse(self, response):
        next_page = response.xpath('//a[@class="_1IHWd _6Nb0L _37aW8 ljjt- f-test-button-dalshe f-test-link-Dalshe"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath('//span[@class="-gENC _1TcZY Bbtm8"]//@href').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_vacancy)

    def parse_vacancy(self, response: HtmlResponse):
        name = response.xpath('//h1[@class="KySx7 Oert7 _2APER Q0JS1 _2L5ou _1TcZY Bbtm8"]/text()').get()
        salary = response.xpath('//span[@class="_2eYAG -gENC _1TcZY dAWx1"]/text()').getall()
        url = response.url
        yield JobparserItem(name=name, salary=salary, url=url)