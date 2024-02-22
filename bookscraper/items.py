# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

def serialize_price(value): 
    # Formatar os price excluding tax que estao vindo zoado é só colocar 
    # na classe abaixo scrapy.Field().(serialize=serialize_price)
    # como vamos fazer um pipeline, vamos fazer isso la

    return f'£ {str(value)}'

# class BookscraperItem(scrapy.Item):
#     define the fields for your item here like:
#     name = scrapy.Field()





class BookItem(scrapy.Item):

    url = scrapy.Field()
    title= scrapy.Field()
    product_type = scrapy.Field()
    price_excl_tax = scrapy.Field()
    price_incl_tax = scrapy.Field()
    tax= scrapy.Field()
    availability = scrapy.Field()
    num_reviews= scrapy.Field()
    stars= scrapy.Field()
    category=scrapy.Field()
    description=scrapy.Field() 
    price=scrapy.Field()

pass