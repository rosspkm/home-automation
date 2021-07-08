from pymongo.common import validate
import db.connect as connection
import ErrorHandler.errors as error
import cmds.keywords as keywords

def receive_data(data: dict):
    hub_id = data["hub_id"]
    cmd = data["text"]

    hub = connection.mongo.check_hub(hub_id)

    if hub:
        lookup(cmd)
        words = cmd.split(" ")
        parsed = parse_data(words)
        parsed = convert(parsed)
        devices = get_devices(parsed, hub, hub_id)
        if devices:
            return devices



        else:
            return "an unexpected error has occured please try again"


    else:
        return "please make sure this hub is connected to your account and try again"


def parse_data(words: list):
    
    parsed = {}
    for k, types in keywords.items():
        if type(types) is dict:
            for key, values in types.items():
                for x in values:
                    if x in words:
                        parsed[k] = types
                        parsed["cmd"] = x
                        words.remove(x)
        else:
            for k, t in keywords.items():
                for x in t:
                    if x in words:
                        parsed[k] = x
                        words.remove(x)
    return parsed


def convert(parsed):
    for key, value in keywords.device_structure.items():
        if parsed['device'] == key:
            parsed['device'] = value
    
    for key, value in keywords.cmd_switch.items():
        if parsed['cmd'] == key:
            parsed['cmd'] = value
    
    return parsed


def get_devices(parsed, hub, hub_id):
    hub_data = hub['hubs'][hub_id]['devices']
    device_triggers = {}
    for key in hub_data.keys():
        if hub_data[key]['device_type'] == parsed['device'] and hub_data[key]['location'] == parsed["location"]:
            device_triggers[key] = parsed['cmd']
    return device_triggers


def lookup(cmd: str):
