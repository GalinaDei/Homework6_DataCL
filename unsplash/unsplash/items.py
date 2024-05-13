# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UplushImgItem(scrapy.Item):
    author_image = scrapy.Field()
    description = scrapy.Field()
    categories = scrapy.Field()
    Published = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
