import json
import os

from dotenv import load_dotenv
from pokemon_repository import PokemonRepository

load_dotenv()


def insert_initial_data(repo):
    with open('./pokemon.json') as f:
        data = json.load(f)
    return repo.insert_many(data)


if __name__ == '__main__':
    repository = PokemonRepository(os.getenv('MONGO_URL'), 'test', 'pokemon')
    # insert_initial_data(repository)

    # nameで検索
    results = repository.find(filter={"name": "フシギダネ"})
    for result in results:
        print(result)

    # projection
    # skip, limit, sort
    # AND検索
    # OR検索
    # 部分一致
    # 範囲検索
    # トランザクション https://pymongo.readthedocs.io/en/stable/api/pymongo/client_session.html
