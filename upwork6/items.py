# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Upwork6Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    country_name = scrapy.Field()
    region_name = scrapy.Field()
    cities_name = scrapy.Field()

    

