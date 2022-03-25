from operator import contains
import os
import scrapy

class TV2Spider(scrapy.Spider):
    name = 'tv2'
    start_urls = ['https://nyheder.tv2.dk/rusland-invaderer-ukraine']
    custom_settings = {
        'FEEDS': {
            os.path.join('data', 'tv2_items.json'): {'format': 'json'}
        }
    }

    def parse(self, response):
        for teaser in response.css('.tc_teaser'):
            label = teaser.css('.tc_label')
            label_text = label.css('::text').get().lower()
            print(label_text)
            if 'rusland invaderer ukraine' in label_text:
                title = teaser.css('.tc_heading')
                text = title.css('::text').get()
                yield {'title': text}