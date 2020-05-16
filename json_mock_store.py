from abstract_json_storage import AbstractJsonStorage


class JsonMockstore(AbstractJsonStorage):
    def __init__(self):
        super().__init__()

    def get_name(self):
        return "reqres.in"

    def create(self, json_data, session):
        return self._request(session, "post", "/api/users?delay=2", json_data)

    async def update(self, store_id, json_data):
        pass

    async def read(self, store_id):
        # return self._get(session, "/api/users?delay=2", json_data)
        pass

    def _get_api_root(self):
        return "https://reqres.in"

