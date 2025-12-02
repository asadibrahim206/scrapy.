
from scrapy import Item,Field
from itemloaders.processors import MapCompose, TakeFirst


def get_number(txt):
    return float(txt.replace("$",""))

class EbookItem(Item):
    # define the fields for your item here like:
    title = Field(
        TakeFirst()
    )
    price = Field(
        input_processor = MapCompose(get_number),
        output_processor = TakeFirst()
    )
   
