from abstract_json_storage import AbstractJsonStorage


class JsonMockstore(AbstractJsonStorage):
    def __init__(self):
        super().__init__()

    def create(self, json_data, session):
        return self._post(session, "/api/users?delay=2", json_data)

    async def update(self, store_id, json_data):
        pass

    async def read(self, store_id):
        pass

    def _get_api_root(self):
        return "https://reqres.in"

