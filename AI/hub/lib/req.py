import lib.config as config
import main
import json

class request:

    def __init__(self):
        self.hub_id = config.device_id
        self.account_id = config.account_id
    
    def get_hub_id(self):
        return self.hub_id
    
    def get_account_id(self):
        return self.account_id


def parse(msg):
    info = request()

    send = {
        "hub_id": info.get_hub_id(),
        "text": msg

    }
    return main.process(json.dumps(send))
