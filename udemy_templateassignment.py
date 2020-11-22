from flask import Flask , url_for , render_template , request

app = Flask(__name__)



@app.route("/")
def fun_1():
    return render_template('templateassignmentinherit.html')


@app.route("/home")
def fun_2():
    return render_template('my_home.html')

@app.route("/home/enter")
def fun_3():
    return render_template('tempassign_enter.html')

@app.route("/home/result")
def fun_4():
    val = request.args.get('val')

    flag1 = False
    flag2 = False

    for i in val:
        if i.isdigit():
            flag1 = True
        elif i.isupper():
            flag2 = True

    if flag1 and flag2:
        return render_template('result_templateassign.html',flag1=flag1,flag2=flag2)
    else:
        return render_template('result_templateassign.html')




if __name__ == '__main__':
    app.run(debug=True)