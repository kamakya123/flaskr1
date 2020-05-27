from flask import Flask
from flask_restx import *
from pymongo import MongoClient
app = Flask(__name__)

api = Api(app,version='1.0',title='excel_API',description="getting the required from the database")


client = MongoClient()

app.config.from_pyfile('database.py')

app.config.from_pyfile('main.py')

from database import *

from main import *


if __name__=='__main__':
    app.run(debug=True)
