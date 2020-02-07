import os
import json
import datetime

from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/igmDb1"
mongo = PyMongo(app)
app.json_encoder = JSONEncoder

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contactme", methods=['GET', 'POST', 'DELETE', 'PATCH'])
def contactme():
    return render_template("contactme.html")

@app.route("/contactinput", methods=['POST'])
def contactinput():
    print(request.form["test"])
    return render_template("contactme.html")
   # return jsonify(data), 200

@app.route("/actiontest", methods=['POST'])
def actiontest():
    if request.method == 'POST':
        comms_collection = mongo.db.comms
        print("----------POST begins--------------")
        query2 = request.form['messagebody']
        print(query2)
        comms_collection.insert_one({'firstname' : 'Test', 'lastname': 'Guy', 'email': '1', 'address': '2', 'city': '','country':'','reason':'', 'message':query2})
        print("----------------POST COMPLETED--------------")
        return render_template("contactme.html"), 200
    else:
        return render_template("contactme.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
