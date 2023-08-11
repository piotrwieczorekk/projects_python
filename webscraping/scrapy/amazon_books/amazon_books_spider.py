import scrapy
import time
from amazon_books_scrap.items import title_fix, strip_value, price_fix, pages_fix, BookItem
import random

class AmazonBooksSpiderSpider(scrapy.Spider):
    name = "amazon_books_spider"
    allowed_domains = ["www.amazon.pl"]
    start_urls = ["https://www.amazon.pl/s?rh=n%3A22743434031&fs=true&ref=lp_22743434031_sar"]
    
    def parse(self, response):
        book_links =  response.xpath('//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]//a/@href').getall()
        for book_link in book_links:
            correct_link = 'https://www.amazon.pl' + book_link
            yield response.follow(correct_link, callback=self.parse_book_page)
            time.sleep(3)
        
        next_page_url = f'''https://www.amazon.pl{response.xpath('//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]/@href').get()}'''
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)
            time.sleep(3)

    
    def parse_book_page(self, response):
        book_item = BookItem()
    
        book_title = response.xpath('(//div[@class="a-section a-spacing-none"]//h1[@id="title"]//span/text())[1]').get()
        if book_title:
            book_item['book_title'] = title_fix(book_title)
        else:
            book_item['book_title'] = None
        
        book_author = response.xpath('//span[@class="author notFaded"]//a/text()').get()
        if book_author:
            book_item['book_author'] = strip_value(book_author)
        else:
            book_item['book_author'] = None
        
        customer_reviews_count = response.xpath('//div[@id="averageCustomerReviews"]//span[@class="a-declarative"]//a[@id="acrCustomerReviewLink"]//span/text()').get()
        if customer_reviews_count:
            book_item['customer_reviews_count'] = strip_value(customer_reviews_count)
        else:
            book_item['customer_reviews_count'] = None
        
        try:
            book_price = response.xpath('//span[@id="price"]/text()').get()
            if book_price:
                book_item['book_price'] = price_fix(book_price)
        except:
            book_price = response.xpath('//span[@class="slot-price"]/text()').get()
            if book_price:
                book_item['book_price'] = price_fix(book_price)
        
        pages = response.xpath('(//div[@class="a-carousel-viewport"]//div[@class="a-section a-spacing-none a-text-center rpi-attribute-value"])[1]//span/text()').get()
        if pages:
            book_item['pages'] = pages_fix(pages)
        else:
            book_item['pages'] = None
        
        language = response.xpath('(//div[@class="a-carousel-viewport"]//div[@class="a-section a-spacing-none a-text-center rpi-attribute-value"])[2]//span/text()').get()
        if language:
            book_item['language'] = strip_value(language)
        else:
            book_item['language'] = None
        
        publisher = response.xpath('(//div[@class="a-carousel-viewport"]//div[@class="a-section a-spacing-none a-text-center rpi-attribute-value"])[3]//span/text()').get()
        if publisher:
            book_item['publisher'] = strip_value(publisher)
        else:
            book_item['publisher'] = None

        yield book_item

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
    