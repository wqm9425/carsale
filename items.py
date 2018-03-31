# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CarsaleItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    vin = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    parameter = scrapy.Field()
    packages = scrapy.Field()
    
