from flask_restful import Resource, reqparse
from models.trail_trajectory import TrailTrajectoryModel
from sqlalchemy.exc import SQLAlchemyError


class TrailTrajectory(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "lat",
        type=str,
        required=True,
        help="Latitude value in decimal degrees (required)",
    )
    parser.add_argument(
        "lon",
        type=str,
        required=True,
        help="Longitude value in decimal degrees (required)",
    )
    parser.add_argument(
        "elev", 
        type=str,
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
        """
        data.lat = [float(num) for num in data.lat.split(',')]
        data.lon = [float(num) for num in data.lon.split(',')]
        data.elev = [float(num) for num in data.elev.split(',')]
        
        for i in len(data.lat):
            data = (id,data.lat[i],data.lon[i],data.elev[i])
            trail_trajectory = TrailTrajectoryModel(**data)

            try:
                trail_trajectory.upsert()
            except SQLAlchemyError as e:
                return {"message": f"An error occurred while uploading trail trajectory.{e}"}, 500


        """

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