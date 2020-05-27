from __init__ import *
from database import *
from filehandler import *

api = Blueprint('app',__name__)

@api.route('/')
def HOME():
    return render_template('search.html')

@api.route('/search')
def search():
    return redirect(url_for('app.HOME'))

@api.route('/success', methods= ['POST'])
def success():
    ip_url= request.form['search']
    
    q = use.find_one({"ip_address":ip_url})
    s = use.find_one({"url": ip_url})
    k = user.find_one({"url": ip_url})
    l = my.find_one({"url":ip_url})
    m = al.find_one({"url":ip_url})
    if q:
    
        output = {"ip_address": q["ip_address"],"vendorName": q["vendorName"],"technical_Owner": q["technical_Owner"],"url":q["url"]}
        
        return render_template('database.html',result=output) 
    if s:     
        
        output = {"ip_address": s["ip_address"],"vendorName": s["vendorName"],"technical_Owner": s["technical_Owner"],"url":s["url"]}
        return render_template('database.html',result=output) + session['output']
        
    if k:
        output = {"APP-Id":k["APP-Id"],"vendorName":k["vendorName"],"technical_Owner":k["technical_Owner"],"url":k["url"] }
        return render_template('database.html',result=output)
    if l:
        output = {"technical_Owner":l["technical_Owner"],"url":l["url"],"vendorName":l["vendorName"]}
        return render_template('database.html',result=output)
    if m:
        output = {"Model":m["Model"],"technical_Owner":m["technical_Owner"],"vendorName":m["vendorName"],"url":m["url"]}
        return render_template('database.html',result=output)
    else:
        output = {'data': 'No Data found'}
        return render_template('database.html',result=output)


@api.route('/shodan')
def shodan():
    return redirect("https://www.shodan.io/", code = 302)