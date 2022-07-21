import json
import os

from dotenv import load_dotenv
from pymongo import ASCENDING, DESCENDING

from pokemon_repository import PokemonRepository

load_dotenv()


def insert_initial_data(repo):
    with open("./pokemon.json") as f:
        data = json.load(f)
    return repo.insert_many(data)


if __name__ == "__main__":
    repository = PokemonRepository(os.getenv("MONGO_URL"), "test", "pokemon")
    repository.create_collection()
    insert_initial_data(repository)

    # nameで検索
    # results = repository.find(filter={"name": "フシギダネ"})
    # for result in results:
    #     print(result)

    # projectionでフィールドを指定、$inで配列に含む文字列を指定
    # results = repository.find(
    #     projection={"_id": False, "name": True, "types": True},
    #     filter={"types": {"$in": ["みず"]}},
    #     limit=10,
    # )
    # for result in results:
    #     print(result)

    # ネストしたオブジェクトのフィールドで検索
    # results = repository.find(
    #     projection={"_id": False, "name": True, "stats": True},
    #     filter={"stats.hp": 130},
    #     limit=10,
    # )
    # for result in results:
    #     print(result)

    # skip, limit, sort
    # results = repository.find(
    #     projection={"_id": False, "name": True, "types": True, "abilities": True},
    #     filter={"types": {"$in": ["ほのお"]}},
    #     skip=10,
    #     limit=10,
    #     sort=[("name", DESCENDING)]
    # )
    # for result in results:
    #     print(result)

    # AND検索
    results = repository.find(
        projection={"_id": False, "name": True, "types": True, "abilities": True},
        filter={'$and': [{"types": {"$all": ["くさ", "どく"]}}, {"abilities": {"$all": ["しんりょく"]}}]},
        limit=10,
    )
    for result in results:
        print(result)

    # 部分一致
    # results = repository.find(
    #     projection={"_id": False, "name": True, "types": True, "abilities": True},
    #     filter={"name": {"$regex": "ブ"}},
    #     limit=10,
    # )
    # for result in results:
    #     print(result)

    # 範囲検索
    # results = repository.find(
    #     projection={"_id": False, "name": True, "stats": True},
    #     filter={"stats.attack": {"$gte": 131, "$lte": 135}},
    #     sort=[("stats.attack", DESCENDING)],
    #     limit=10,
    # )
    # for result in results:
    #     print(result)

    # トランザクション https://pymongo.readthedocs.io/en/stable/api/pymongo/client_session.html
