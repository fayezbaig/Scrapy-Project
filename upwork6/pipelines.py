# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class Upwork6Pipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'fayezr135',
            database = 'mydatabase'

        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS mydatabase""")
        self.curr.execute("""create table mydatabase(
                          country_name text,
                          region_name text,
                          cities_name text
                        )""")
        
    def process_item(self,item,spider):
        self.store_db(item)
        return item
    
    def store_db(self,item):
        self.curr.execute("""insert into mydatabase values (%s,%s,%s)""", (
            item['country_name'],
            item['region_name'],
            item['cities_name'],
        ))

        self.conn.commit()

