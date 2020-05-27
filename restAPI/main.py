from __init__ import *
from database import *
ns = api.namespace('ip_url',description='ip or  url serach')
model = api.model('ip/url',{
        'ip_address' : fields.String(readonly=True),
        'url'        : fields.String(readonly=True),
        'vendorName' : fields.String(readonly=True),
        'technical_Owner' : fields.String(readonly=True)
})
    

@ns.route('/ip_address/url/<ip_url>')    
class Mydb(Resource):
    @ns.doc('get the fields of data using eighter by typing ip_address or url')
    @ns.marshal_with(model)
    def get(self,ip_url):
        'Get one data'
        q = use.find_one({"ip_address":ip_url})
        s = use.find_one({"url": ip_url})
        k = user.find_one({"url": ip_url})
        l = my.find_one({"url":ip_url})
        m = al.find_one({"url":ip_url})
        if q:
    
            output = {"ip_address": q["ip_address"],"vendorName": q["vendorName"],"technical_Owner": q["technical_Owner"],"url":q["url"]}
        
            return output
        if s:     
        
            output = {"ip_address": s["ip_address"],"vendorName": s["vendorName"],"technical_Owner": s["technical_Owner"],"url":s["url"]}
            return output
        
        if k:
            output = {"APP-Id":k["APP-Id"],"vendorName":k["vendorName"],"technical_Owner":k["technical_Owner"],"url":k["url"] }
            return output
        if l:
            output = {"technical_Owner":l["technical_Owner"],"url":l["url"],"vendorName":l["vendorName"]}
            return output
        if m:
            output = {"Model":m["Model"],"technical_Owner":m["technical_Owner"],"vendorName":m["vendorName"],"url":m["url"]}
            return output
        else:
            output = {'data': 'No Data found'}
            return output
   