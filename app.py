
from flask import Flask, jsonify, request# For flask implementation
from pymongo import MongoClient
from flask_pymongo import PyMongo
from bson import Binary, Code
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask_cors import CORS

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
mydb = client["candidateportal"]
mycol = mydb["candidate"]

cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['MONGO_DBNAME']='candidateportal'
app.config['MONGO_URI']='mongodb://localhost:27017/'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def get_all_lists():
    #name=mongo.db.Bhavana
    #result=name.find()
    mydoc = mycol.find()

    return dumps(mydoc)
    #return jsonify(mydoc)



    

if __name__ == "__main__":
    app.run(debug=True)