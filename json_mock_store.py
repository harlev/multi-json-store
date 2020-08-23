import json
from abstract_json_storage import AbstractJsonStorage


class JsonMockstore(AbstractJsonStorage):
    def __init__(self):
        super().__init__()

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

    def _get_api_root(self):
        return "https://reqres.in"

