import sqlite3
from db import db


class TrailRatingModel(db.Model):
    __tablename__ = "tblTrail_Rating"
    rating_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String(20), nullable=False)

    def __init__(self, rating_id, rating):
        self.rating_id = rating_id
        self.rating = rating

    def json(self):
        return {"rating_id": self.rating_id, "rating": self.rating}

    @classmethod
    def find_by_rating(cls, rating):
        return cls.query.filter_by(rating=rating).first()

    def upsert(self):
        db.session_add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
