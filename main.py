import json
import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


class MongoRepository:

    def __init__(self, db_name, coll_name):
        self.client = MongoClient(os.getenv('MONGO_URL'))
        self.db = self.client[db_name]
        self.collection = self.db.get_collection(coll_name)

    def find(self, projection=None, skip=0, limit=0, filter=None, sort=None):
        return self.collection.find(projection=projection, skip=skip, limit=limit, filter=filter, sort=sort)

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def insert_many(self, documents):
        return self.collection.insert_many(documents)


def mongo_import(repository: MongoRepository):
    with open('./pokemon.json') as f:
        data = json.load(f)
    return repository.insert_many(data)


if __name__ == '__main__':
    repository = MongoRepository('test', 'pokemon')
    # mongo_import(repository)
    results = repository.find(filter={"name": "フシギダネ"})
    for result in results:
        print(result)
