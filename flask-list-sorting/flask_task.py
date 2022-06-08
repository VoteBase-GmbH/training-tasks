from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

class List_sort(Resource):
  
    def post(self):
        int_list = json.loads(request.form['data'])
        int_list.sort()
        return(jsonify({'sorted_list':int_list}))

api.add_resource(List_sort, "/")

if __name__ == "__main__":
    app.run()