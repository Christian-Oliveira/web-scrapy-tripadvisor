from gc import callbacks
import scrapy

from tripadvisor.items import TripadvisorItem


class CommentsSpider(scrapy.Spider):
    name = 'comments'
    allowed_domains = ['tripadvisor.com.br']
    start_urls = ['https://www.tripadvisor.com.br/Hotel_Review-g60763-d93419-Reviews-The_Carlyle_A_Rosewood_Hotel-New_York_City_New_York.html#REVIEWS']

    def parse(self, response):
        item = TripadvisorItem()
        comment_boards = response.xpath("//div[@class='cWwQK MC R2 Gi z Z BB dXjiy']")
        for board in comment_boards:
            item['author'] = board.xpath(".//div[@class='bcaHz']/span/a/text()").get()
            item['address'] = board.xpath(".//span[@class='default ShLyt small']/text()").get()
            item['title'] = board.xpath(".//span[@lang='pt-x-mtfrom-en']/span/text()").get()
            item['comment'] = board.xpath(".//div[@class='pIRBV _T']/q/span/text()").get()
            item['date_published'] = board.xpath(".//span[@class='euPKI _R Me S4 H3']/text()").get().strip(" ")
            yield item
            
        exists_next_page = response.xpath("//a[@class='ui_button nav next primary ' and text()='Próximas']/@href").get()
        if exists_next_page:
            yield response.follow(url=exists_next_page, callback=self.parse)