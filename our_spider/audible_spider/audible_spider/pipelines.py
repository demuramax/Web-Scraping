# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import pymongo
import sqlite3

# class MongodbPipeline:
#     collection_name = 'audible_books'
    
#     def open_spider(self, spider): 
#          logging.warning('Spider Opened - Pipeline')
#          self.client = pymongo.MongoClient("mongodb+srv://demuramax:demuramax@cluster0.s5jwb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#          self.db = self.client['My_Database']
         
#     def close_spider(self, spider): 
#         self.client.close()
    
#     def process_item(self, item, spider):
#         self.db[self.collection_name].insert(item)
#         return item

class SQLitePipeline:

    def open_spider(self, spider):
        # create database file
        self.connection = sqlite3.connect('audible.db')
        # we need a cursor object to execute SQL queries
        self.c = self.connection.cursor()
        #  try/except will help when running this for the +2nd time (we can't create the same table twice)
        
        # query: create table with columns
        self.c.execute('''
            CREATE TABLE audible (
                title TEXT,
                author TEXT,
                length TEXT,
                url TEXT,
            ) m''')
    # save changes
        self.connection.commit()


    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        # query: insert data into table
        self.c.execute('''
            INSERT INTO audible (title,author,length, url) VALUES(?,?,?,?)
        ''', (
            item.get('title'),
            item.get('author'),
            item.get('length'),
            item.get('url'),
        ))
        # save changes
        self.connection.commit()
        return item