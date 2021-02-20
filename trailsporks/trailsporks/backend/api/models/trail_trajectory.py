import sqlite3
from db import db


class TrailTrajectoryModel(db.Model):
    __tablename__ = "tblTrail_Trajectory"
    pkey = db.Column(db.Integer, primary_key=True)
    trail_id = db.Column(db.Integer)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    elev = db.Column(db.Float)

    def __init__(self, trail_id, lat, lon, elev):
        self.trail_id = trail_id
        self.lat = lat
        self.lon = lon
        self.elev = elev

    def json(self):
        return {
            "id": self.trail_id,
            "lat": self.lat,
            "lon": self.lon,
            "elev": self.elev,
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(trail_id=id).first()

    def upsert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
