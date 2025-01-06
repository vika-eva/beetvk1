from pprint import pprint

import requests
import json

URL = 'https://api.nasa.gov/planetary/apod'
api_key = 'qOdRW9eU7kggJmrc8pOQVxQtpV7lUZvjNlFkgjbL'

def func():
    date = '2024-12-22'
    params = {
        'api_key': api_key,
        'date': date,
        'hd': 'True'
    }
    response = requests.get(URL, params=params).json()
    #pprint(response)
    return response

res = func()
with open('task_2_33_result.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=4)