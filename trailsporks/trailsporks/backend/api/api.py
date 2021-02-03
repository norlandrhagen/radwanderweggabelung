from flask import Flask
from flask_restful import Resource, Api
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = # URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(Trail, '/trail/<string:name>')
api.add_resource(TrailMetadata, '/trailmetadata/<string:name>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000)