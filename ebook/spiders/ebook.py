import scrapy
from ebook.items import EbookItem
from scrapy.loader import ItemLoader

class EbookScraper(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]  # Fixed: start_urls not url

    def parse(self, response):
        print("[PARSE]")  # Fixed typo in "PARSE"
    
        ebooks = response.css("article.product_pod")

        for ebook in ebooks:
            loader = ItemLoader(item=EbookItem())
            loader.add_value('title', ebook.css("h3 a").attrib['title'])
            loader.add_value('price',ebook.css("p.price_color::text") )
        

            yield loader.load_item()  