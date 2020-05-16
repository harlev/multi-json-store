from unittest import TestCase
from abstract_json_storage import AbstractJsonStorage
from json_store import JsonStore


class TestStore(TestCase):
    def setUp(self):
        self.js = JsonStore()

    def test_init_storage(self):
        for store in self.js.stores:
            isinstance(store, AbstractJsonStorage)

    def test_create(self):
        self.js.create({"a": 1})
        pass
