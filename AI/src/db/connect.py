import pymongo
import ErrorHandler.errors as error

class mongo:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")

    def check_hub(self, data):
        db = self.client.accounts
        col = db.account_id
        try:
            return col.find({"hubs": {data["hub_id"]}})
        except:
            return None

    def find_device(self, data: list):
        return True
