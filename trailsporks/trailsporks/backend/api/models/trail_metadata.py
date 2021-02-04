import sqlite3
from db import db

class TrailMetadataModel(db.Model):
    __tablename__ = "trailmetadata"  # Table names need to be shored up.
    pkey = db.Column(db.Integer, primary_key=True)
    trail_id = db.Column(db.Integer)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    elev = db.Column(db.Float)

    def __init__(self, trail_id, lat, lon, elev):
        trail_id = trail_id
        lat = lat
        lon = lon
        elev = elev
    
    def json(self):
        return {'id': self.trail_id, 'lat': self.lat, 'lon': self.lon, 'elev': self.elev}

    @classmethod
    def find_by_id(self,id):
        return cls.query.filter_by(trail_id=id)

    def upsert(self):
        db.session_add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()