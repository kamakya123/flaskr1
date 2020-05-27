from __init__ import *
from database import *

csv1 = 'csv/call.csv'
csv2 = 'csv/app.csv'
csv3 = 'csv/set.csv'
csvFilePath = 'csv/request.csv' #csvfile name

jsonFilePath = 'json/new.json'   # jsonfile name
jsonf1 = 'json/call.json'
jsonf2 = 'json/app.json'
jsonf3 = 'json/set.json'

#opening the csv file and reading as dictionary and stroring in a  list
with open (csvFilePath) as csvFile: 
    csvReader = csv.DictReader(csvFile)
    data = []
    for row in csvReader:
        data.append(row)

with open(csv1) as c1:
    out1 = []
    csvreader1 = csv.DictReader(c1)
    for row1 in csvreader1:
        out1.append(row1)

with open(csv2) as c2:
    out2 = []
    csvr1 = csv.DictReader(c2)
    for row2 in csvr1:
        out2.append(row2)
with open(csv3) as c3:
    out3 = []
    csvr2 = csv.DictReader(c3)
    for row3 in csvr2:
        out3.append(row3)


with open(jsonFilePath,'w') as File:       #opening the json file and writing the list data to the jsonfile
   new  = File.write(json.dumps(data,indent=4))

with open(jsonf1,'w') as File:       #opening the json file and writing the list data to the jsonfile
   all  = File.write(json.dumps(out1,indent=4))


with open(jsonf2,'w') as File:       #opening the json file and writing the list data to the jsonfile
   some  = File.write(json.dumps(out2,indent=4))

with open(jsonf3,'w') as File:       #opening the json file and writing the list data to the jsonfile
   do = File.write(json.dumps(out3,indent=4))

with open(jsonFilePath,'r') as f:        #opening the jsonfile and reading it and converting json to python dictionary
    one = json.load(f)

with open(jsonf1,'r') as f1:        #opening the jsonfile and reading it and converting json to python dictionary
    js1 = json.load(f1)


with open(jsonf2,'r') as f2:        #opening the jsonfile and reading it and converting json to python dictionary
    js2 = json.load(f2)

with open(jsonf3,'r') as f3:        #opening the jsonfile and reading it and converting json to python dictionary
    js3 = json.load(f3)



def insert():
    res_= use.insert_many(one)     #if you want to insert the data uncomment the res
    rep_ = user.insert_many(js1)
    rec_ = my.insert_many(js2)
    rel_ = al.insert_many(js3)
insert()


app.config.from_pyfile('app.py')
from app import *