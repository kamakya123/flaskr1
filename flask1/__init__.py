from flask import Blueprint
from flask import *
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('localhost,27017')

app.secret_key='b_5#y2L"F4Q8z\n\xec]/'

app.config.from_pyfile('database.py')

from database import *

from login import kam


app.register_blueprint(kam)


if __name__=="__main__":
    app.run(debug = True)