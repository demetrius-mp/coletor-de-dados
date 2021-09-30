from __future__ import annotations

import os
from functools import wraps
from typing import Optional

import requests
from dotenv import load_dotenv

import adapter


def get(url: str, headers: Optional[dict] = None):
    return requests.get(url, headers=headers).json()


def key_required(f):
    @wraps(f)
    def decorated_func(self: API = None):
        if not self.key:
            raise ValueError('This API requires a key.')

        return f(self)

    return decorated_func


class API:
    def __init__(self, file: os.PathLike | bytes | str, key: Optional[str] = None):
        self.file = file
        self.key = key

    @key_required
    def coinlib(self):
        url = f'https://coinlib.io/api/v1/coinlist?key={self.key}&pref=BRL&page=1&order=rank_asc'
        coins: list[dict] = get(url)['coins'][:50]
        adapter.save_as_csv(coins, self.file)

    @key_required
    def fortnitetracker(self):
        headers = {
            'TRN-Api-Key': self.key
        }

        url = f'https://api.fortnitetracker.com/v1/store'
        store_info = get(url, headers)[:50]
        adapter.save_as_csv(store_info, self.file)

    def rickandmorty(self):
        list_of_characters = list(range(1, 51))
        url = f'https://rickandmortyapi.com/api/location/{list_of_characters}'
        locations: list[dict] = get(url)
        for loc in locations:
            loc.update({
                'residents': len(loc['residents'])
            })

        adapter.save_as_csv(locations, self.file)


def test_rickandmorty():
    file = 'rickandmorty.csv'
    api = API(file)
    api.rickandmorty()


def test_fortnitetracker():
    file = 'fortnitetracker.csv'
    key = os.environ.get('fortnitetracker_key')
    api = API(file, key)
    api.fortnitetracker()


def test_coinlib():
    file = 'coinlib.csv'
    key = os.environ.get('coinlib_key')
    api = API(file, key)
    api.coinlib()


def main():
    load_dotenv()
    test_rickandmorty()
    test_coinlib()
    test_fortnitetracker()


if __name__ == '__main__':
    main()
