import os
import scrapy
import datetime as dt
from nltk import word_tokenize

class DRSpider(scrapy.Spider):
    name = 'dr'
    start_urls = ['https://www.dr.dk/nyheder/tema/krig-i-ukraine']
    custom_settings = {
        'FEEDS': {
            os.path.join('data', 'dr_items.json'): {'format': 'json'}
        }
    }

    def parse(self, response):
        year = dt.datetime.today().year

        for teaser in response.css('.dre-teaser-list__item'):
            time_text = teaser.css('.dre-teaser-meta-label').css('::text').getall()[1].lower().strip()

            if time_text.startswith('i går'):
                time = self.yesterday_label_to_datetime(time_text, year)
            else:
                time = self.full_time_label_to_datetime(time_text, year)

            title = ' '.join(teaser.css('.dre-title-text').css('::text').getall())
            yield {
                'time': time,
                'title': title
            }

    def yesterday_label_to_datetime(self, time_text, year):
        yesterday = dt.datetime.today() - dt.timedelta(days=1)
        time_split = word_tokenize(time_text)
        hour_mins = time_split[-1].split(':')
        return dt.datetime(year, yesterday.month, yesterday.day, int(hour_mins[0]), int(hour_mins[1]))

    def full_time_label_to_datetime(self, time_text, year):
        clean_time = time_text.replace('.', '').replace('kl', '')
        time_split = word_tokenize(clean_time)
        day = int(time_split[0])
        month = self.to_month_num(time_split[1])
        hour_mins = time_split[2].split(':')
        time = dt.datetime(year, month, day, int(hour_mins[0]), int(hour_mins[1]))
        return time


    def to_month_num(self, month:str):
        if month.startswith('jan'):
            return 1
        elif month.startswith('feb'):
            return 2
        elif month.startswith('mar'):
            return 3
        elif month.startswith('apr'):
            return 4
        elif month.startswith('maj'):
            return 5
        elif month.startswith('jun'):
            return 6
        elif month.startswith('jul'):
            return 7
        elif month.startswith('aug'):
            return 8
        elif month.startswith('sep'):
            return 9
        elif month.startswith('okt'):
            return 10
        elif month.startswith('nov'):
            return 11
        elif month.startswith('dec'):
            return 12