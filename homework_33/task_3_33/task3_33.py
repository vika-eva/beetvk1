import requests, json

city = input("enter city name: ")
try:
    url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=613aea5d1ea63571d6dc6e691400aa2b'
    res = requests.get(url.format(city=city))
    data = res.json()

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']


    print('Temperature:',int(temp) - 273,'°C')
    print('Wind:',wind)
    print('Pressure: ',pressure)
    print('Humidity: ',humidity)
    print('Description:',description)
except Exception:
    print(f'cant find {city}')

with open('weather.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=4)
