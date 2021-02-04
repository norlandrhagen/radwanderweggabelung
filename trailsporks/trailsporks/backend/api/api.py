from flask import Flask
from flask_restful import Resource, Api
from db import db

from resources.trail_res import Trail
from resources.trailmetadata_res import TrailMetadata

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = # URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(Trail, '/trail/<string:name>')
api.add_resource(TrailMetadata, '/trailmetadata/<int:id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000)
