from openpyxl import Workbook
from itemadapter import ItemAdapter

class EbookPipeline:

    def open_spider(self, spider):
        # Create workbook and get active sheet
        self.workbook = Workbook()
        self.sheet = self.workbook.active  # lowercase 'w'!
        self.sheet.title = "ebooks"
        
        # Add headers (not spider.cols - that doesn't exist)
        self.sheet.append(["Title", "Price"])  # Add your column headers here

    def process_item(self, item, spider):
        # Append item data to sheet
        self.sheet.append([
            item.get('title', ''),  # Use .get() for safety
            item.get('price', '')
        ])
        return item
  
    def close_spider(self, spider):  # lowercase 'spider' and correct method name
        # Save the workbook
        self.workbook.save("ebook.xlsx")