# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentHrSpiderItem(scrapy.Item):
    # 职位名
    postionName = scrapy.Field()
    # 职位详情链接
    postionLink = scrapy.Field()
    # 职位类别
    postionType = scrapy.Field()
    # 招聘人数
    peopleNumber = scrapy.Field()
    # 工作地点
    workLocation = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()
