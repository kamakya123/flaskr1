from __init__ import *

db = client.mydb
use = db.col # collection 1
user = db.ravi # collection 2
my = db.swetha # collection 3
al = db.kamakya # collection 4

def drop():
    use.drop()
    user.drop()
    my.drop()
    al.drop()
#drop()
app.config.from_pyfile('app.py')
app.config.from_pyfile('filehandler.py')

from app import *
from filehandler import *