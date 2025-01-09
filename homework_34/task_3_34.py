import requests, json, threading

url = 'https://api.nasa.gov/planetary/apod'
api_key = 'qOdRW9eU7kggJmrc8pOQVxQtpV7lUZvjNlFkgjbL'

def func(res: list):
    start_date = '2019-02-22'
    end_date = '2020-02-23'
    params = {'api_key': api_key, 'start_date': start_date, 'end_date': end_date}
    r = requests.get(url, params)
    res.append(r.json())

if __name__ == '__main__':

    res = []
    threads = []
    for i in range(2):
        threads.append(threading.Thread(target=func, args=(res,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    with open('res3.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, indent=4)


