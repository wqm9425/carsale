import scrapy
from urllib.parse import urljoin
from carsale.items import CarsaleItem

class CarsaleSpider(scrapy.spiders.Spider):
    name = 'BMV_cars'
    start_urls = ['https://www.knauzbmw.com/used-inventory/index.htm?start=0&']

    def __init__(self):
        self.base_url = 'https://www.knauzbmw.com/used-inventory/index.htm'

    def parse(self, response):
    	inventorys = response.css('div.bd>ul.inventoryList.full.list-unstyled>li')
    	for inventory in inventorys:
    		title = inventory.css('div.hproduct.auto>div>h3.fn>a.url::text').extract()
    		vin = inventory.css('div.hproduct.auto::attr(data-vin)').extract()
    		link = inventory.css('div.hproduct.auto>div>div.media>a::attr(href)').extract()
    		price = inventory.css('span.final-price>span.value::text').extract()

    		features = inventory.css('div.description>dl>dt::text').extract()
    		values = inventory.css('div.description>dl>dd::text').extract()
    		parameter = {}
    		for feature, value in zip(features, values):
    			parameter[feature] = value

    		packages = inventory.css('div.packages>span.packageTitle::text').extract()

    		yield CarsaleItem(title = title, vin = vin, link = link, price = price,\
    			parameter = parameter, packages = packages)

    	next_page_url = response.css('a.btn.btn-link.btn-xs[rel=next]::attr(href)').extract()[0]
    	if next_page_url is not None:
    		yield scrapy.Request(urljoin(self.base_url, next_page_url))





