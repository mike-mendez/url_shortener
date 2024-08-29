from .schemas.url import Url


class DummyDatabase:
    urls: dict[int, Url] = {}


db = DummyDatabase()
