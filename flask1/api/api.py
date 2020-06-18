from flask import *
from flask_restx import Resource, Api, fields

app = Flask(__name__)
api = Api(app)

model = api.model('model', {
    'name':fields.string,
    'address': fields.string,
    'date_updated': fields.DateTime(dt_format='rfc822')
})

@api.route('/todo')
class Todo(resource):
    @api.marshal_with(model,envelope='resource')
    def get(self,**kwargs):
        return db_get_todo()
if __name__=='__main__':
    app.run(debug = True)
