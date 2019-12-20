# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class YgSpider(CrawlSpider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    # 定义提取url地址规则
    rules = (
        # 连接提取器，提取url地址；处理提取的response；当前url地址的响应是否重新经过rules来提取url地址
        Rule(LinkExtractor(allow=r'http://wz.sun0769.com/html/question/201908/\d+.shtml'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'http://wz.sun0769.com/index.php/question/questionType?type=4&page=\d+'), follow=True),
    )

    def parse_item(self, response):
        item = {}
        item["content"] = response.xpath("//td[@class='txt16_3']//text()").extract()
        item["content_img"] = response.xpath("//td[@class='txt16_3']//img/@src").extract()
        item["content_img"] = ["http://wz.sun0769.com" + i for i in item["content_img"]]
        # return item
        print(item)
