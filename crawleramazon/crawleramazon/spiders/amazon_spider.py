import scrapy


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.de/s?k=Books&crid=2ZC63KF6C6HCR&sprefix=books%2Caps%2C160&ref=nb_sb_noss_1']

    def parse(self, response):
        pass
