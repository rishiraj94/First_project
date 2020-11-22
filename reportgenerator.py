from flask import Flask , render_template


app = Flask(__name__)



@app.route('/')
def fun_1():

    return 'welcome'


@app.route('/report')
def fun_2():

    a = int(input('enter a marks out of 100 ').strip())

    b = int(input('enter b marks out of 100').strip())

    c = int(input('enter c marks out of 100').strip())

    di = dict([('amark',a),('bmark',b),('cmark',c)])

    print(di)

    return render_template('report.html',di=di)


if __name__ == "__main__":
    app.run(debug=True)