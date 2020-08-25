from unittest import TestCase
import json
from abstract_json_storage import AbstractJsonStorage
from json_store import JsonStore


class TestStore(TestCase):
    def setUp(self):
        self.js = JsonStore()

    def test_init_storage(self):
        for store in self.js.stores:
            isinstance(store, AbstractJsonStorage)

    def test_create(self):
        self.js.create('{"a": 1}')

    def test_read(self):
        self.js.create('{"a": 2}')
        results = self.js.read()
        for result in results:
            self.assertDictEqual({"a": 2}, json.loads(result["result"]))

    def test_update(self):
        self.js.create('{"a": 2}')
        self.js.update(json_data='{"a": 3}')
        results = self.js.read()
        for result in results:
            self.assertDictEqual({"a": 3}, json.loads(result["result"]))