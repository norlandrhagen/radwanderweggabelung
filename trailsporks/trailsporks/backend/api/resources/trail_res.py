from flask_restful import Resource, reqparse
from models.trail import TrailModel


class Trail(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "difficulty",
        type=str,
        required=False,
        default="Do you know the rating of this trail?",
        help="Trail rating: Service Road, Green, Blue, Black, Double Black.",
    )
    parser.add_argument(
        "description",
        type=str,
        required=False,
        default="Enter a description for this trail!",
        help="Description of the trail.",
    )

    def get(self, name):
        trail = TrailModel.get_by_name(name)
        if trail:
            return trail.json()
        return {"message": "trail not found"}, 404

    def post(self, name):
        if TrailModel.get_by_name(name):
            return {"message": "A trail with this name already exists."}, 400

        data = Trail.parser.parse_args()
        trail = TrailModel(name, **data)
        try:
            trail.upsert()
        except:
            return {"message": "An error occurred uploading the trail."}, 500

        return trail.json(), 201

    def put(self, name):
        data = Trail.parser.parse_args()
        trail = TrailModel.get_by_name(name)
        if trail is None:
            trail = TrailModel(name, **data)
        else:
            if data.description:
                trail.description = data.description
            if data.difficulty:
                trail.difficulty = data.difficulty
        try:
            trail.upsert()
            return {"Updated Trail:": trail.json()}
        except:
            return {"message": "An error occurred updating the trail."}, 500

    def delete(self, name):
        trail = TrailModel.get_by_name(name)
        if trail:
            trail.delete()
            return {"message": "Trail deleted."}
        return {"message": "A trail with the provided name does not exist."}, 404

class TrailList(Resource):
    def get(self):
        return {'Trails': [trail.json() for trail in TrailModel.query.all()]}

