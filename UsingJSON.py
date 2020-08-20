#!/usr/bin/env python3

import json
import requests

people = [
    {
    "name":"Sabrina Green",
    "username": "sgreen",
    "phone": {
        "office": "802-867-5309",
        "cell": "802-867-5310"
    },
    "department":"IT Infrastructure",
    "role":"Systems Administrator"
    },
    {
    "name":"Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127",
        },
        "department":"IT Infrastructure",
        "role":"IT Specialist"
    }
]

people_json = json.dumps(people)
print("JSON OUTPUT:")
print(people_json)
print()

print("WEBSITE RESPONSE:")
response = requests.get('https://www.google.com', stream=True)
print(response.raw.read()[:100])
