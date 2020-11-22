from flask import Flask
from flask_restful import Resource , Api

app = Flask(__name__)
api = Api(app)

lst = []
lst1 = []


class bengaluru(Resource):

    def post(self,name):
        d = {'place':name}
        lst.append(d)
        return d

    def get(self,name):
        for i in lst:
            if i['place'] == name:

                return i

        return {'place':'not found !'},404

    def delete(self,name):
        count = 0
        for i in lst:

            if i['place'] == name:
                remmov = lst.pop(count)

                return {'removed':remmov}

            count += 1
        return {'place':'not found'},404


class mumbai(Resource):

    def post(self, name):
        d = {'place': name}
        lst1.append(d)
        return d

    def get(self, name):
        for i in lst1:
            if i['place'] == name:
                return i

        return {'place': 'not found !'}, 404

    def delete(self, name):
        count = 0
        for i in lst1:

            if i['place'] == name:
                remmov = lst.pop(count)

                return {'removed': remmov}

            count += 1
        return {'place': 'not found'}, 404


class all(Resource):

    def get(self):

        return {'places':lst}

class allmum(Resource):

    def get(self):

        return {'places':lst1}

api.add_resource(bengaluru,'/bengaluru/<name>')
api.add_resource(mumbai,'/mumbai/<name>')
api.add_resource(all,'/places/bengaluru')
api.add_resource(allmum,'/places/mumbai')

if __name__ == "__main__":
    app.run(debug=True)