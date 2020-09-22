import json
from abstract_json_storage import AbstractJsonStorage


class JsonMockstore(AbstractJsonStorage):
    def __init__(self):
        super().__init__()
        self.update_called = False

    def get_name(self):
        return "reqres.in"

    def create(self, session, json_data=None, store_id=None):
        return self._request(session, "post", "/api/users?delay=2", json_data)

    def update(self, session, json_data=None, store_id=None):
        return self._request(session, "put", "/api/users/2", json_data)

    def read(self, session, json_data=None, store_id=None):
        return self._request(session, "get", "/api/users/2")

    def result_callback(self, method_name, result_content):
        if method_name == "create":
            content = json.loads(result_content)
            object_id = content["id"]
            self._set_store_id(object_id)
        if method_name == "read":
            return '{"a": 3}' if self.update_called else '{"a": 2}'
        if method_name == "update":
            self.update_called = True

    def _get_api_root(self):
        return "https://reqres.in"

