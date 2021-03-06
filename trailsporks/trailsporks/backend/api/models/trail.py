import sqlite3
from db import db


class TrailModel(db.Model):
    __tablename__ = "tblTrails"
    trail_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    difficulty = db.Column(db.String(30))
    description = db.Column(db.String(500))

    def __init__(self, name, difficulty="Do you know the rating of this trail?",
        description="Enter a description for this trail!"):
        self.name = name
        self.difficulty = difficulty
        self.description = description

    def json(self):
        return {"trail_id":self.trail_id,"name": self.name, "difficulty": self.difficulty,
        "description": self.description}

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def upsert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
