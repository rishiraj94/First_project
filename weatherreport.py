from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
from datetime import date


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///weather.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class old_weatherdata(db.Model):

    __tablename__ = "weatherdata"

    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.Text)
    maxtemp = db.Column(db.Integer)
    mintemp = db.Column(db.Integer)
    condition = db.Column(db.Text)

    def __init__(self,date,maxtemp,mintemp,condition):
        self.date = date
        self.maxtemp = maxtemp
        self.mintemp = mintemp
        self.condition = condition

    def __repr__(self):
        return "the max temp is {} min temp is  {} on {}".format(self.maxtemp,self.mintemp,self.date)


@app.route('/')
def fun_1():
    return "WELCOME FLASK WEATHER REPORT <a href='/report'>CLICK HERE TO SEE WEATHER REPORT </a>"

@app.route('/report')
def fun_2():
    var = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + 'bengaluru' + '&appid=2c58efac117b2df8e7181375cd290be6').json()



    temp = var['main']['temp'] - 273.15
    tempmin = var['main']['temp_min'] - 273.15
    maxtemp = var['main']['temp_max'] - 273.15
    feels = var['main']['feels_like'] - 273.15



    day = date.today()

    j = old_weatherdata.query.all()
    v = old_weatherdata.query.get(len(j))

    if v.date != str(day):
        print('inside')
        db.create_all()
        inst = old_weatherdata(str(day),maxtemp,tempmin,var['weather'][0]['description'])
        db.session.add(inst)
        db.session.commit()
        j = old_weatherdata.query.all()
        return render_template('weatherreport.html', day=day, var=var, j=j)
    else:
        print('out')
        return render_template('weatherreport.html',day=day,var=var,j=j)


if __name__ == "__main__":
    app.run(debug=True)