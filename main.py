import pymongo
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import datetime
import pprint

#Auth protection

#protection via .py file with password:
from credits import password

#protection via .env file with password
# 1. pip install python-dotenv
# 2. create file with password
from dotenv import load_dotenv
import os
def configure():
    load_dotenv()
#Load .env file
configure()

client = pymongo.MongoClient(f"mongodb+srv://PetrsMongoDB:{os.getenv('password')}@cluster0.t98rxzh.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
print(client)
mydb = client['sample_supplies']
mycol = mydb["sales"]

#Поиск нескольких записей по параметру
#myquery = { "storeLocation": "Denver" }
#mydoc_myquery = mycol.find(myquery)
#for x in mydoc_myquery:
#  print(x)

#Поиск одной записи
#mydoc_one = mycol.find_one()
#print(mydoc_one)
#mydoc_sort = mycol.find().sort("saleDate", -1)
#for x in mydoc_sort:
#    print(x)

#Поиск нескольких записей по дате
d = datetime.datetime(2013, 11, 12, 12)
for post in mycol.find({"saleDate": {"$lt": d}}).sort("saleDate"):
    pprint.pprint(post['saleDate'])
    pprint.pprint(post['purchaseMethod'])