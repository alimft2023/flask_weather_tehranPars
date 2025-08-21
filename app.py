from flask import Flask, render_template, request
from models import Weather
import datetime
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        url = 'https://api.openweathermap.org/data/2.5/weather'
        q = city
        appid = '6ad934a76186d5d2fb596a8e925a0cae'
        units = 'metric'
        try:
            res = requests.get(
                url=url, params={'q': q, 'appid': appid, 'units': units}).json()
            temp = res['main']['temp']
            pressure = res['main']['pressure']
            humidity = res['main']['humidity']
            description = res['weather'][0]['description']
            date = datetime.datetime.now()
            icon = res['weather'][0]['icon']
            Weather.create(temp=temp, pressure=pressure,
                           humidity=humidity, description=description, date=date, icon=icon, city=city)
            return render_template('index.html', res=res)
        except KeyError:
            error = 'city not found!'
            return render_template('index.html', error=error)

    elif request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
