# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

from .settings import CSV_DIR
import os

class GethouescsvPipeline(object):
    def __init__(self):
        fname = os.path.join(CSV_DIR, 'sz_house.csv')

        self.file = open(fname, 'a+', newline='', encoding='utf-8')

        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        self.writer.writerow([item['name'], item['rant'], item['root_type'],
                              item['area'], item['decoration'],
                              item['elevator'], item['toward'],
                              item['url']])
        return item

    def close_spider(self, spider):
        self.file.close()
        print('保存租屋信息完成！')