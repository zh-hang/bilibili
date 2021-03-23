# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class BilibiliPipeline:
    filename = 'bilibiliVideo.json'

    def open_spider(self, spider):
        self.f = open(self.filename, 'w')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        try:
            line = json.dumps(item)
            self.f.write(line + '\n')
        except:
            pass
        return item
