import scrapy


class CommentsSpider(scrapy.Spider):
    name = 'comments'
    allowed_domains = ['tripadvisor.com.br']
    start_urls = ['http://tripadvisor.com.br/']

    def parse(self, response):
        pass
