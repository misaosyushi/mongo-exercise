from dotenv import load_dotenv
from pymongo import MongoClient, ReadPreference

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

    def list_databases(self):
        print(self.client.list_database_names())

    def count(self):
        return self.collection.count_documents({})

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def insert_many(self, documents):
        return self.collection.insert_many(documents)

    def insert_many_with_transaction(self, documents):
        with self.client.start_session() as session:
            with session.start_transaction():
                self.collection.insert_many(documents, session=session)

    def create_collection(self):
        self.collection.drop()
        pokemon_schema = {
            "bsonType": "object",
            "required": ["no", "name", "form", "isMegaEvolution", "types"],
            "properties": {
                "no": {
                    "bsonType": "int"
                },
                "name": {
                    "bsonType": "string"
                },
                "form": {
                    "bsonType": "string"
                },
                "isMegaEvolution": {
                    "bsonType": "bool"
                },
                "types": {
                    "bsonType": "array"
                }
            }
        }
        self.db.create_collection("pokemon", validator={"$jsonSchema": pokemon_schema})
