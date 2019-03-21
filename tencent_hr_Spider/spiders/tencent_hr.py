# -*- coding: utf-8 -*-
import scrapy

from tencent_hr_Spider.items import TencentHrSpiderItem


class TencentHrSpider(scrapy.Spider):
    # 爬虫名称
    name = "tencent_hr"
    # 爬取域名范围
    allowed_domains = ["tencent.com"]
    # 需要格式化的url地址
    baseURL = 'http://hr.tencent.com/position.php?&start={}#a'
    # url地址的偏移量
    offset = 0
    # 起始url
    start_urls = [baseURL.format(str(offset))]

    def parse(self, response):
        # 构建item对象，用来保存数据
        item = TencentHrSpiderItem()
        # 提取每个response的数据
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:
            # 提取每个职位的信息，并且将提取出的Unicode字符串以UTF-8编码
            # postionName = node.xpath("./td[1]/a/text()")[0].extract()
            # postionLink = node.xpath("./td[1]/a/@href")[0].extract()
            # postionType = node.xpath("./td[2]/text()")[0].extract()
            # peopleNumber = node.xpath("./td[3]/text()")[0].extract()
            # workLocation = node.xpath("./td[4]/text()")[0].extract()
            # publishTime = node.xpath("./td[5]/text()")[0].extract()
            # item['postionName'] = postionName
            # item['postionLink'] = postionLink
            # item['postionType'] = postionType
            # item['peopleNumber'] = peopleNumber
            # item['workLocation'] = workLocation
            # item['publishTime'] = publishTime

            # # 方法1：条件判断
            # if len(node.xpath("./td[1]/a/text()")):
            #     item['postionName'] = node.xpath("./td[1]/a/text()")[0].extract()
            # else:
            #     item['postionName'] = ''
            #
            # if len(node.xpath("./td[1]/a/@href")):
            #     item['postionLink'] = node.xpath("./td[1]/a/@href")[0].extract()
            # else:
            #     item['postionLink'] = ''
            #
            # if len(node.xpath("./td[2]/text()")):
            #     item['postionType'] = node.xpath("./td[2]/text()")[0].extract()
            # else:
            #     item['postionType'] = ''
            #
            # if len(node.xpath("./td[3]/text()")):
            #     item['peopleNumber'] = node.xpath("./td[3]/text()")[0].extract()
            # else:
            #     item['peopleNumber'] = ''
            #
            # if len(node.xpath("./td[4]/text()")):
            #     item['workLocation'] = node.xpath("./td[4]/text()")[0].extract()
            # else:
            #     item['workLocation'] = ''
            #
            # if len(node.xpath("./td[5]/text()")):
            #     item['publishTime'] = node.xpath("./td[5]/text()")[0].extract()
            # else:
            #     item['publishTime'] = ''

            # 方法2：捕捉异常
            try:
                item['postionName'] = node.xpath("./td[1]/a/text()")[0].extract()
            except:
                item['postionName'] = ''

            try:
                item['postionLink'] = node.xpath("./td[1]/a/@href")[0].extract()
            except:
                item['postionLink'] = ''

            try:
                item['postionType'] = node.xpath("./td[2]/text()")[0].extract()
            except:
                item['postionType'] = ''

            try:
                item['peopleNumber'] = node.xpath("./td[3]/text()")[0].extract()
            except:
                item['peopleNumber'] = ''

            try:
                item['workLocation'] = node.xpath("./td[4]/text()")[0].extract()
            except:
                item['workLocation'] = ''

            try:
                item['publishTime'] = node.xpath("./td[5]/text()")[0].extract()
            except:
                item['publishTime'] = ''
            print('-' * 200, item['peopleNumber'])

            # return item返回item对象给引擎，然后终止parse(self, response)函数，不再往后执行parse(self, response)函数中的代码。
            # return item

            # yield item返回item对象给引擎，然后继续往后执行parse(self, response)函数中的代码。
            yield item

        # 拼接url，适用场景是“没有可以点击的请求链接，必须通过拼接url才能获取响应”的场合。
        if self.offset <= 3050:
            self.offset += 10
            url = self.baseURL.format(str(self.offset))
            # 构建下一页的请求，并返回给引擎
            yield scrapy.Request(url, callback=self.parse)
