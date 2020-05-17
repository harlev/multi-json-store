from abstract_json_storage import AbstractJsonStorage


class JsonMockstore(AbstractJsonStorage):
    def __init__(self):
        super().__init__()

    def get_name(self):
        return "reqres.in"

    def create(self, json_data, session):
        return self._request(session, "post", "/api/users?delay=2", json_data)

    def update(self, store_id, json_data):
        pass

    def read(self, store_id, session):
        return self._request(session, "get", "/api/users/2")

    def _get_api_root(self):
        return "https://reqres.in"

