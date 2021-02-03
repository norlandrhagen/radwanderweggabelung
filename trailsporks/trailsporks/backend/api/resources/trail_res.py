from flask_restful import Resource, reqparse
from models.trail import TrailModel

class Trail(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help='The name of the trail (required)'
    )

    def get(self, name):
        trail = TrailModel.get_by_name(name)
        if trail:
            return trail.json()
        return {'message': 'trail not found'}, 404
        
    def post(self, name):
        if TrailModel.get_by_name(name):
            return {'message':'A trail with this name already exists.'}
        
        data = Trail.parser.parse_args()
        trail = TrailModel(data)

        try:
            trail.upsert()
        except:
            return {'message': 'An error occurred uploading the trail.'}, 500

        return trail.json(), 201 

    def delete(self, name):
        trail = TrailModel.get_by_name(name)
        if trail:
            trail.delete()
        return {'message': 'Trail deleted.'} 

    