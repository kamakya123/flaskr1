from flask import *
from pymongo import MongoClient
import csv
import os
app = Flask(__name__)

client = MongoClient()




app.config.from_pyfile('database.py')

app.config['SERVER_NAME'] = 'localhost:5000'

app.config.from_pyfile('filehandler.py')

app.secrect_key = os.urandom(24)

app.config.from_pyfile('run.py')

from run import *

from database import *

from app import api

from filehandler import * 

app.register_blueprint(api)

