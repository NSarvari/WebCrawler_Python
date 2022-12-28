import scrapy
from ..items import CrawleramazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.de/s?k=Books&crid=2ZC63KF6C6HCR&sprefix=books%2Caps%2C160&ref=nb_sb_noss_1']

    def parse(self, response):
        items = CrawleramazonItem()

        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        product_price = response.css('.s-price-instructions-style .a-price-whole').css('::text').extract()
        product_image = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_image'] = product_image

        yield items
