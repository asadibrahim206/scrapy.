import scrapy

class EbookScraper(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]  # Fixed: start_urls not url

    def parse(self, response):
        print("[PARSE]")  # Fixed typo in "PARSE"
    
        ebooks = response.css("article.product_pod")
        for ebook in ebooks:
            title = ebook.css("h3 a").attrib['title']