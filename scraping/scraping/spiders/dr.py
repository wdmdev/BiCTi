import os
import scrapy

class DRSpider(scrapy.Spider):
    name = 'dr'
    start_urls = ['https://www.dr.dk/nyheder/tema/krig-i-ukraine']
    custom_settings = {
        'FEEDS': {
            os.path.join('data', 'dr_items.json'): {'format': 'json'}
        }
    }

    def parse(self, response):
        for title in response.css('.dre-title-text'):
            yield {'title': title.css('::text').get()}