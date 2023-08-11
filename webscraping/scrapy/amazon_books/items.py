# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AmazonBooksScrapItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass


def price_fix(value):
    value = value.replace(' zł','')
    value = value.replace(',','.')
    value = value.strip()
    value = float(value)
    return value

def strip_value(value):
    value = value.strip()
    return value

def title_fix(value):
    value = value.strip()
    value = value.title()
    return value

def pages_fix(value):
    value = value.strip()
    value = value.replace(' str.','')
    value = int(value)
    return value

class BookItem(scrapy.Item):
    book_title=scrapy.Field(input_processor = title_fix)
    book_author=scrapy.Field(input_processor = strip_value)
    customer_reviews_count=scrapy.Field(input_processor = strip_value)
    book_price=scrapy.Field(input_processor=price_fix)
    pages = scrapy.Field(input_processor = pages_fix)
    language = scrapy.Field(input_processor = strip_value)
    publisher = scrapy.Field(input_processor = strip_value)
    