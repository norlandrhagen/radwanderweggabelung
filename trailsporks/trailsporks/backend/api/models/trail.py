import sqlite3
from db import db

class TrailModel(db.Model):
    __tablename__ = "trails"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def json(self):
        return {'name': self.name}

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    def upsert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()