# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import os
from pydispatch import dispatcher
from scrapy import signals


class ProvincePipeline(object):

    def __init__(self):
        ###获取spider_closed信号
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def process_item(self, item, spider):
        # # 如果已经存在同名txt文件，则先删除
        # if os.path.exists('C:\\file\\court.txt'):
        #     os.remove('C:\\file\\court.txt')
        self.file = codecs.open('C:\\file\\court.txt', 'ab', encoding='utf-8')
        for c_name in item['name_list']:
            self.file.write(c_name.encode('utf-8')+',')
        return item

    def spider_closed(self, spider, reason):
        if reason == "finished":
            self.file.close()