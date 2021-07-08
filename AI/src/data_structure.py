account_structure = {
    "account_id": {
        "username": "", # required & must be unique
        "password": "", # required
        "email": "", # required
        "phone_number": "", # not required

        "address": { # this is not required
            "street_1": "",
            "street_2": "",
            "city": "",
            "zip_code": ""
        },

        "hubs" : {
            "hub_id": {
                "devices": {
                    "device_id": {
                        "device_type": "",
                        "location": ""
                    }
                }
            }
        },

        "locations": [
            "upstairs",
            "downstairs",
            "kitchen",
            "bedroom"
        ]
    }
}

request_structure = {
    "account_id": "",
    "hub_id": "",
    "request": {
        "device_id": "",
        "request_id": "",
        "request_parameters": ""

    }
}
