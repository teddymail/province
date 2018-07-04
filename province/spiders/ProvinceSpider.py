# -*- coding: utf-8 -*-
import scrapy

from province.items import ProvinceItem

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ProvinceSpider(scrapy.Spider):
    name = "province"
    allowed_domains = ["www.lawtime.cn"]
    start_urls = ["http://www.lawtime.cn/fayuan/"]

    court = []


    def parse(self, response):
        # 获取各省份链接
        a_num = response.xpath('//div[@class="mainplace"]/p/a')
        prov_num = len(a_num)
        a_list = []
        for proy in range(1, prov_num+1):
            a_href = response.xpath('//div[@class="mainplace"]/p/a['+str(proy)+']/@href').extract()
            if len(a_href) == 1:
                a_list.append(a_href[0])
        zxs_list = ['http://www.lawtime.cn/fayuan/city/beijing', 'http://www.lawtime.cn/fayuan/city/chongqing',
                    'http://www.lawtime.cn/fayuan/city/shanghai', 'http://www.lawtime.cn/fayuan/city/tianjin',]
        last_prov = ['http://www.lawtime.cn/fayuan/province/shandong', 'http://www.lawtime.cn/fayuan/province/zhejiang',
                     'http://www.lawtime.cn/fayuan/province/hunan', 'http://www.lawtime.cn/fayuan/province/xizang',
                     'http://www.lawtime.cn/fayuan/province/gansu',]
        wrong_list = ['http://www.lawtime.cn/fayuan/province/ganshu', 'http://www.lawtime.cn/fayuan/province/beijing',
                      'http://www.lawtime.cn/fayuan/province/chongqing', 'http://www.lawtime.cn/fayuan/province/shanghai',
                      'http://www.lawtime.cn/fayuan/province/tianjin']
        for a in a_list:
            if a in zxs_list:
                yield scrapy.Request(a, callback=self.handle_city)
            else:
                if a not in wrong_list:
                    yield scrapy.Request(a, callback=self.handle_prov)
        for a in last_prov:
            yield scrapy.Request(a, callback=self.handle_prov)
        for a in zxs_list:
            yield scrapy.Request(a, callback=self.handle_city)
        print 'over'

    def handle_prov(self, response):
        city_num = len(response.xpath('//div[@class="midarea ma2"]/div[@class="mcol"]'))
        for num in range(2, city_num+2):
            more_link = response.xpath('//div[@class="midarea ma2"]/div['+str(num)+']/h2/span/a/@href').extract()
            if len(more_link) == 1:
                print 'more_link:', more_link
                yield scrapy.Request(more_link[0], callback=self.handle_city)
                # yield scrapy.Request('http://www.lawtime.cn/fayuan/city/beijing', callback=self.handle_city)  # test

    def handle_city(self, response):
        # item = ProvinceItem()
        # # 1.获取法院名称
        # court_list = []
        # num = len(response.xpath('//div[@class="midarea ma2"]/div[@class="mcol"]/dl').extract())
        # for i in range(1, num+1):
        #     court_name = response.xpath('//div[@class="midarea ma2"]/div[@class="mcol"]/dl['+str(i)+']/dt[1]/a/@text').extract()
        #     if len(court_name) == 1:
        #         court_list.append(court_name[0])
        #         print court_name
        # item['name_list'] = court_list

        # 2.获取所有链接
        link_set = set([])
        link_set.add(response.url)
        num = len(response.xpath('//div[@class="midarea ma2"]/div[@class="mcpage c0165B8"]/p/a').extract())
        for i in range(1, num+1):
            link = response.xpath('//div[@class="midarea ma2"]/div[@class="mcpage c0165B8"]/p/a['+str(i)+']/@href').extract()
            if len(link) == 1:
                link_set.add(link[0])
        for link in link_set:
            yield scrapy.Request(link, callback=self.save_name, dont_filter=True)  # dont_filter禁止去重
        # print 'over'

    def save_name(self, response):
        item = ProvinceItem()
        # 1.获取法院名称
        court_list = []
        num = len(response.xpath('//div[@class="midarea ma2"]/div[@class="mcol"]/dl').extract())
        for i in range(1, num+1):
            court_name = response.xpath('//div[@class="midarea ma2"]/div[@class="mcol"]/dl['+str(i)+']/dt[1]/a/text()').extract()
            if len(court_name) == 1:
                court_list.append(court_name[0])
                # print court_name
        # print court_list
        item['name_list'] = court_list
        yield item