import pymongo
import json
from pymongo import MongoClient, InsertOne
from dotenv import load_dotenv
from pathlib import Path, os
import fundamentus as fd


# Connection with the database
load_dotenv()
client = pymongo.MongoClient(str(os.getenv('DATABASE_CONNECTION_STRING')))
db = client.eazy_indicator
collection = db.IBOVstocks_indicators
requesting = []


df = fd.get_resultado()
papers = df.index

for i in range(len(papers)):
  doc_name = f'\\raw_data_{papers[i]}.json'
  with open(f"C:\\Users\\gusta\\OneDrive\\Desktop\\Projetos-Web\\Flask\\eazy_indicator\\backend\\data\\{doc_name}") as f:
    for jsonObj in f:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)
client.close()