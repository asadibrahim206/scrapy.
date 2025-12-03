from scrapy import Spider

class Ebook_Scraper(Spider):
    name = "ebooks"
    url = ["https://books.toscrape.com/"]

    def parse(self,response):
        print("[ PARSE ]")
        ebook = response.css("h3 a::text")
        print(ebook)