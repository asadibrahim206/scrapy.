from openpyxl import workbook
from itemadapter import ItemAdapter


class EbookPipeline:
    def open_spider(self,Spider):
        self.workbook = workbook()
        self.sheet = self.workbook.active
        self.sheet.title = "ebooks"
        self.sheet.append(Spider.cols)
        
    def process_item(self, item, spider):
        self.sheet.append([item['title'],item['price']])
  
    def close(self,Spider):
        self.workbook.save("ebook.xlsx")