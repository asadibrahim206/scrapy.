from scrapy import Item,Field
from itemloaders.processors import MapCompose,TakeFirst


def change_currency(str):
    return float(str.replace("£",""))

class EbookItem(Item):
    # define the fields for your item here like:
    title = Field(
         output_processor = TakeFirst()
    )
    price = Field(
        input_processor = MapCompose(change_currency),
        output_processor = TakeFirst()
    ) 
   
