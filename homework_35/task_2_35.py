import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from pprint import pprint

import requests
import json
import concurrent.futures
import functools
import time


url = 'https://api.nasa.gov/planetary/apod'
api_key = 'qOdRW9eU7kggJmrc8pOQVxQtpV7lUZvjNlFkgjbL'

def func(res: list):
    start_date = '2019-02-22'
    end_date = '2019-02-23'
    params = {'api_key': api_key, 'start_date': start_date, 'end_date': end_date}
    r = requests.get(url, params)
    res.append(r.json())
    return res



def pr_func(res: list):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(func, [res])



if __name__ == '__main__':


    with multiprocessing.Manager() as manager:
        res = manager.list()
        pr_func(res)
        copy_res = list(res)

    with open('res3.json', 'w', encoding='utf-8') as f:
        json.dump(copy_res, f, indent=4)

