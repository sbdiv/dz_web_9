import json
import pymongo

def upload_to_mongodb(file_name, collection_name):
    
    client = pymongo.MongoClient("link")
    db = client["first_bd"]
    collection = db[collection_name]
    
    with open(file_name) as f:
        data = json.load(f)
        collection.insert_many(data)

if __name__ == "__main__":
    upload_to_mongodb('authors.json', 'authors') 
    upload_to_mongodb('quotes.json', 'quotes')    
