# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

# from scrapy.conf import settings
from scrapy.exceptions import DropItem
import json
import csv

from airbnb.items import Listing


class CSVPipeline:

    def open_spider(self, spider):
        self.file = open('{}.csv'.format(spider.name), 'w')
        self.writer = csv.writer(self.file)
        
        self.written_header = False


    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):

        row = dict(item)
        
        if not self.written_header:
            self.writer.writerow(row.keys())
            self.written_header = True

        self.writer.writerow(row.values())

        return item


class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = open(spider.name + '.jsonl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):

        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item


class MongoPipeline:

    collection_name = 'listings'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item
