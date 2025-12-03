from scrapy import Spider
from ebook.items import EbookItem
from scrapy.loader import ItemLoader


            
class Ebook_Scraper(Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/catalogue/category/books/travel_2/"]
    cols = ['title','price']
    def parse(self,response):
        print("[ PARSE ]")
        ebooks = response.css("article.product_pod")

        for ebook in ebooks:
            loader = ItemLoader(item =EbookItem(), selector=ebook)
            # title = ebook.css("h3 a::attr(title)").get()
            # ebook_item["title"] = ebook.css("h3 a").attrib["title"]
            # ebook_item["price"] =change_currency(ebook.css("p.price_color::text").get())

            loader.add_css('title', "h3 a::attr(title)")
            loader.add_css('price', "p.price_color::text")

            yield loader.load_item()
            
