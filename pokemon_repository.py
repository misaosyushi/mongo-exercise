from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


class PokemonRepository:
    def __init__(self, mongo_url, db_name, coll_name):
        self.client = MongoClient(mongo_url)
        self.db = self.client[db_name]
        self.collection = self.db.get_collection(coll_name)

    def find(self, projection=None, skip=0, limit=0, filter=None, sort=None):
        return self.collection.find(
            projection=projection, skip=skip, limit=limit, filter=filter, sort=sort
        )

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def insert_many(self, documents):
        return self.collection.insert_many(documents)
