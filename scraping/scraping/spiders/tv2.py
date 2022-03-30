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
            label = teaser.css('.tc_label::text').get().lower().strip()
            if 'rusland invaderer ukraine' == label:
                url = teaser.css('a::attr(href)').get()
                yield scrapy.Request(url, callback=self.parse_teaser_content)

    
    def parse_teaser_content(self, response):
        title = response.css('.tc_heading::text').get()
        time = response.css('.tc_timestamp::attr(datetime)').get()
        yield {
            'time': time,
            'title': title
        }