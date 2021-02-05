from flask_restful import Resource, reqparse
from models.trail import TrailModel


class Trail(Resource):
    def get(self, name):
        trail = TrailModel.get_by_name(name)
        if trail:
            return trail.json()
        return {"message": "trail not found"}, 404

    def post(self, name):
        if TrailModel.get_by_name(name):
            return {"message": "A trail with this name already exists."}, 400

        trail = TrailModel(name)

        try:
            trail.upsert()
        except:
            return {"message": "An error occurred uploading the trail."}, 500

        return trail.json(), 201

    def put(self, name):
        if TrailModel.get_by_name(name):
            trail = TrailModel(name)
            try:
                trail.upsert()
            except:
                return {"message": "An error occurred updating the trail."}, 500
        return {"message": "A trail with the provided Id does not exist."}

    def delete(self, name):
        trail = TrailModel.get_by_name(name)
        if trail:
            trail.delete()
            return {"message": "Trail deleted."}
        return {"message": "A trail with the provided name does not exist."}, 404
