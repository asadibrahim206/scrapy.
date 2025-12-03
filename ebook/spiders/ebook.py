from scrapy import Spider
from ebook.items import EbookItem

class Ebook_Scraper(Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/catalogue/category/books/travel_2"]

    def parse(self,response):
        print("[ PARSE ]")
        ebooks = response.css("article.product_pod")

        for ebook in ebooks:
            ebook_item = EbookItem
            # title = ebook.css("h3 a::attr(title)").get()
            ebook_item["title"] = ebook.css("h3 a").attrib["title"]
            ebook_item["price"] =ebook.css("p.price_color::text").get()

            yield ebook_item
            
