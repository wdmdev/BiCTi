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
        for teaser in response.css('.dre-teaser-list__item'):
            time = teaser.css('.dre-teaser-meta-label').css('::text').getall()[1]
            title = ' '.join(teaser.css('.dre-title-text').css('::text').getall())
            yield {
                'time': time,
                'title': title
            }