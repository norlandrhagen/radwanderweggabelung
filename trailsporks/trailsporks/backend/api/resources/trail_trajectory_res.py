from flask_restful import Resource, reqparse
from models.trail_trajectory import TrailTrajectoryModel
from sqlalchemy.exc import SQLAlchemyError

# Should we use the nargs or the delimited string approach to pass data?
# It feels like strings might be the way to go?

class TrailTrajectory(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "lat",
        nargs='+'
        type=float,
        required=True,
        help="Latitude value in decimal degrees (required)",
    )
    parser.add_argument(
        "lon",
        nargs='+',
        type=float,
        required=True,
        help="Longitude value in decimal degrees (required)",
    )
    parser.add_argument(
        "elev", 
        nargs='+',
        type=float,
        required=True, 
        help="Elevation in feet (required)"
    )

    def get(self, id):
        trajectory = TrailTrajectoryModel.find_by_id(id)
        if trajectory:
            return [md.json() for md in trajectory], 200
        return {"message": "Trail trajectory not found"}, 404

    def post(self, id):
        if TrailTrajectoryModel.find_by_id(id):
            return {"message": "A trail with this Id already exists."}, 400

        data = TrailTrajectory.parser.parse_args()
        trail_trajectory = TrailTrajectoryModel(id, **data)

        try:
            trail_trajectory.upsert()
        except SQLAlchemyError as e:
            return {"message": f"An error occurred while uploading trail trajectory.{e}"}, 500

        return trail_trajectory.json(), 201

    # Need to correct put logic once we refine approach to pass arrays.
    def put(self, id):
        if TrailTrajectoryModel.find_by_id(id):
            data = TrailTrajectory.parser.parse_args()
            trail_trajectory = TrailTrajectoryModel(id, **data)
            try:
                trail_trajectory.upsert()
            except:
                return {"message": "An error occurred updating trail trajectory."}, 500
        return {"message": "A trail with the provided Id does not exist."}

    def delete(self, id):
        trail_trajectory = TrailTrajectoryModel.find_by_id(id)
        if trail_trajectory:
            trail_trajectory.delete()
            return {"message": "Trail trajectory deleted."}
        return {"message": "Trail with the associated id does not exist."}, 404

class TrajectoryList(Resource):
    def get(self):
        return {'Trajectories': [trail.json() for trail in TrailTrajectoryModel.query.all()]}