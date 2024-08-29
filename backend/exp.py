import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["search_summarizer"]

collection = db["search_results"]
collection.insert_one({"name":"Aranya"})

print(client)