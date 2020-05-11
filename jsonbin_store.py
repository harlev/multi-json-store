from abstract_json_storage import AbstractJsonStorage


class JsonBinStore(AbstractJsonStorage):
    def __init__(self):
        self.homepage = "https://jsonbin.io/"
        super().__init__()
        
    def create(self, json_data):
        pass

    def update(self, store_id, json_data):
        pass

    def read(self, store_id):
        pass

