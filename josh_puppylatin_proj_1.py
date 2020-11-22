#puppy latin rules :-
'''1 . if a puppy name doesnot ends on a y add a y to the end of the name
   2 . ex - rofus -> royusy
   3.  if a puppy name does end in a y , replace it iful insteade
       ex- sparky -> sparkiful
       path - /puppylatin/puppyname'''
from flask import Flask
app = Flask(__name__)


@app.route("/")
def fun_1():
    return "<h1>WELCOM TO FLASK PUPPY LATIN UDEMY ASSIGNMENT API</h1>"

@app.route("/puppylatin")
def fun_2():
    return "<h1>enter the puppy name here puppylatin/your_puppyname</h1>"

@app.route("/puppylatin/<puppyname>")
def fun_3(puppyname):
    newname = ""
    if puppyname[-1] == "y":
        lst = list(puppyname)
        lst.remove("y")
        lst.append("iful")
        newname = "".join(lst)
    elif puppyname[-1] != "y":
        newname = puppyname + "y"

    return "<h1>your puppy name {} in puppy latin is {}</h1>".format(puppyname,newname)

if __name__ == '__main__':
    app.run(debug=True) #running the app in dubugging on mode


