import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017/")


current_db = db_client["dbdbd"]



collection = current_db["messages"]


def get_message():
    for channel in collection.find():
        print(channel['username'], channel['text'])

get_message()
