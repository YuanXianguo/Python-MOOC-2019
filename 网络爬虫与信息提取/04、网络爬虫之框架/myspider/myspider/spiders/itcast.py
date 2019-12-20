# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        """处理start_url地址对应的响应"""
        # ret = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret)

        # 分组
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = dict()
            # item["name"] = li.xpath(".//h3/text()").extract()[0]
            # 提取第一个值，没有返回None
            item["name"] = li.xpath(".//h3/text()").extract_first()
            # item["title"] = li.xpath(".//h4/text()").extract()[0]
            item["title"] = li.xpath(".//h4/text()").extract_first()
            # print(item)
            # 只能返回Request,BaseItem,dict or None
            yield item
