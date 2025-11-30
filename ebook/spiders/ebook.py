import scrapy

class EbookScraper(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]  # Fixed: start_urls not url

    def parse(self, response):
        print("[PARSE]")  # Fixed typo in "PARSE"
    
        ebooks = reponse.css("article")
        for ebook in ebooks:
            title = ebook.css("a::text").get()
            price = ebook.css("p.price_color").get()


