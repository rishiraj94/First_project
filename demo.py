from flask import Flask,render_template,url_for

app = Flask(__name__)


@app.route("/")
def fun_1():
    return "<h1>Flask working</h1>"

@app.route("/level/")
def fun():
    return "<h2>Flask working 2</h2>"

#example of dynamic routing

# @app.route("/<dynamic>")
# def fun_2(dynamic):
#     return "<h1>this ths flask dynamic routhing of {}</h1>".format(dynamic)

@app.route("/<name>")
def funn(name):
    return "<h1>THIS IS FLASK DYNAMIC TEMPLATE {}</h1>".format(name)

#example of a render template
@app.route("/render")
def fun_4():
    return render_template("demo_template.html")

#passing variables to the template and conditional looping
@app.route("/render/a")
def var_1():
    temp = "hello this is 1st variable"
    return render_template("demo_passvariables.html",var=temp)

@app.route("/render/b")
def var_2():
    temp = ["hello" , "this is list" , "passing"]
    return render_template("demo_passvariables.html",lst=temp)

@app.route("/render/c")
def var_3():
    temp = dict([("myname","rishiraj"),("myage",27)])
    return render_template("demo_passvariables.html",d=temp)

@app.route("/render/name/<somename>")
def var_4(somename):
    return render_template("demo_passvariables.html",nam=somename)


if __name__ == '__main__':
    app.run()
