import requests
params = {'q': 'tehran',
          'appid': '6ad934a76186d5d2fb596a8e925a0cae', 'units': 'metric'}
res = requests.get(
    'https://api.openweathermap.org/data/2.5/weather/', params=params).json()
# for key, value in res.items():
#     print(key, value, sep='---')

temp = res['main']['temp']
pressure = res['main']['pressure']
humidity = res['main']['humidity']
description = res['weather'][0]['description']
