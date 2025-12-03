from scrapy import Spider

def Ebook_Scraper(spider):
    name = "ebook"
    url = ["https://books.toscrape.com/"]
    def parse(self,response):
        print(response)
