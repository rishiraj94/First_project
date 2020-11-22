from flask import Flask , render_template , request , url_for

app = Flask(__name__)


@app.route("/")
def fun_1():
    return  render_template('index_temp_forms.html')

@app.route("/login")
def fun_2():
    return render_template('signup_temp_forms.html')

@app.route("/index/image")
def fun_3():
    return render_template('image_temp_forms.html')

@app.route("/index/ty")
def fun_4():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankyou_temp_forms.html',first=first,last=last)


if __name__ == '__main__':
    app.run(debug=True)