import json
import random

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/db")
def db():
    client = MongoClient("mongodb://UserRoot:Admin$123@mongodb-rs1:27001,mongodb-rs2:27002,mongodb-rs3:27003/bank?authSource=admin")

    dbname = client["bank"]
    collection_name = dbname["tickets"]

    i = random.randint(0, 100)
    s = collection_name.find_one({'amount': i})
    str1 = ''.join(str(s))

    return str1

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)