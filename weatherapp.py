from flask import Flask , url_for , render_template
import requests
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SECRECT_KEY'] = 'mysecrectkey'

@app.route('/')
def home():

    info = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + 'bengaluru' + '&appid=2c58efac117b2df8e7181375cd290be6').json()

    print(type(info))

    print(info)

    temperature = info['main']['temp']

    feelslike = info['main']['feels_like']

    mintemp = info['main']['temp_min']

    maxtemp = info['main']['temp_max']

    icon = info['weather'][0]['icon']

    tr = requests.get('https://reqres.in/api/users?page=2').json()



    return render_template('weather.html',temperature=temperature,feelslike=feelslike,mintemp=mintemp,maxtemp=maxtemp , icon=icon , tr=tr)


if __name__ == '__main__':
    app.run(debug=True)