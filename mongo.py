from pymongo import MongoClient


client = MongoClient()
db = client.wizcrow
collection = db.products

def insert_phone_specs(specs):
    collection.insert_one(specs)

def update_phone_reviews(reviews, phone):
    collection.update_one({'product_name': phone}, {'$push': {'reviews': {'$each' : reviews}}})
