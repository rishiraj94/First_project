from flask import Flask
from flask_restful import Api , Resource

app = Flask(__name__)

api = Api(app)

data = []

class f_1(Resource):

    def get(self,name):

        for i in data:

            if i['var'] == name:

                return i

        return {'var':'nodata'},404


    def post(self,name):

        d = {"var": name}
        data.append(d)

        return d


    def delete(self,name):

        c = 0
        for i in data:

            if i['var'] == name:
                s = data.pop(c)
                return s

            c +=1
        return {'var':'nodata'},404



class show_all(Resource):

    def get(self):

        return {'list':data}



api.add_resource(f_1,'/<name>')
api.add_resource(show_all,'/show')



if __name__ == "__main__":
    app.run(debug=True)