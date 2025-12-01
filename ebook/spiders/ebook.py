import scrapy
from ebook.items import EbookItem

class EbookScraper(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]  # Fixed: start_urls not url

    def parse(self, response):
        print("[PARSE]")  # Fixed typo in "PARSE"
    
        ebooks = response.css("article.product_pod")

        for ebook in ebooks:
            Ebook_item = EbookItem()
            Ebook_item['title'] = ebook.css("h3 a").attrib['title']
            Ebook_item['price'] = ebook.css("p.price_color::text").get()

            yield Ebook_item

                
            