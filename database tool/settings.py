from __init__ import *

client = MongoClient()




app.config.from_pyfile('database.py')

app.config['SERVER_NAME'] = 'localhost:5000'
app.config.from_pyfile('database.py')
from database import *