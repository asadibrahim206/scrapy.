
from scrapy import Item,Field


class EbookItem(scrapy.Item):
    # define the fields for your item here like:
    title = Field()
    price = Field()
   
