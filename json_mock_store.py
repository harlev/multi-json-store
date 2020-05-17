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

    def _get_api_root(self):
        return "https://reqres.in"

