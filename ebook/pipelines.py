from openpyxl import Workbook
from itemadapter import ItemAdapter
from pymongo import MongoClient

class EbookPipeline:

    def open_spider(self, spider):
        self.client = MongoClient(
        host="mongodb+srv://asadibrahim208:szabist12@scraping.igukdxu.mongodb.net/?appName=scraping",
        connect = False
        )
        self.collection = self.client.get_database("ebooks").get_collection("travel")
    
    def process_item(self, item, spider):
        self.collection.insert_one(
            ItemAdapter(item).asdict()
        )
        return item
  
    def close_spider(self, spider): 
        self.client.close()