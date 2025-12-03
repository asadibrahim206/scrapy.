from scrapy import Spider

class Ebook_Scraper(Spider):
    name = "ebooks"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self,response):
        print("[ PARSE ]")

        ebook = response.xpath('//article/div[@class = "product_price"]/text()')
        print(ebook)
        
        