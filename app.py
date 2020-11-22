from flask import Flask , render_template , request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import  Migrate

app = Flask(__name__)

app.config['SECRECT_KEY'] = "mysecrectkey"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myvlogspage.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class demo(db.Model):

    __tablename__ = 'dem'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    date = db.Column(db.Text)
    vlog = db.Column(db.Text)
    about = db.Column(db.Text)
    social = db.Column(db.Text)

    def __init__(self,name,date , vlog , about , social):
        self.name = name
        self.date = date
        self.vlog = vlog
        self.about = about
        self.social = social


    def __repr__(self):

        return "my name is {}  {} , {} , {} , {}".format(self.name,self.date,self.vlog,self.about,self.social)




@app.route("/")
def home():

    return render_template('home.html')


@app.route("/log",methods=['GET','POST'])
def log():

    if request.method == "POST":

        try:

            id = request.form['id']
            v = demo.query.get(id)

            db.session.delete(v)
            db.session.commit()
            return redirect(url_for("result"))
        except:

            db.create_all()

            user = request.form['nm']

            date = request.form['date']

            vlog = request.form['vlog']

            about = request.form['yourself']

            social = request.form['social']

            instance = demo(user, date, vlog, about, social)

            db.session.add(instance)

            db.session.commit()

            print(instance)

            return redirect(url_for("result"))

    return render_template('l.html')


@app.route("/vlogs")
def result():

    l = demo.query.all()


    return render_template('blog_page.html', l=l)

@app.route("/edit/<int:id>",methods=['GET','POST'])
def edt(id):
    val = demo.query.get(id)

    if request.method == 'POST':

        a = request.form['name']
        b = request.form['date']
        c = request.form['vlog']
        d = request.form['about']
        e = request.form['social']

        val.name = a
        val.date = b
        val.vlog = c
        val.about = d
        val.social = e


        db.session.commit()


        return redirect(url_for('result'))



    val = demo.query.get(id)

    return render_template('testt.html',val=val)


def dell():
    print("inside delfunction")



if __name__ == "__main__":
    app.run(debug=True)