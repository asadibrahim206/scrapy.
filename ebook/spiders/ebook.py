import scrapy

class EbookScraper(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]  # Fixed: start_urls not url

    def parse(self, response):
        print("[PARSE]")  # Fixed typo in "PARSE"
        print(response)
        
