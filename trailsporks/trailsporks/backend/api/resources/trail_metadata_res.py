from flask_restful import Resource, reqparse
from models.trail_metadata import TrailMetadataModel

class TrailMetadata(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=int,
        required=True,
        help='The trail id (required)'
    )
    parser.add_argument('lat',
        type=float,
        required=True,
        help='Latitude value in decimal degrees (required)'
    )
    parser.add_argument('lon',
        type=float,
        required=True,
        help='Longitude value in decimal degrees (required)'
    )
    parser.add_argument('elev',
        type=float,
        required=True,
        help='Elevation in feet (required)'
    )

    def get(self,id):
        metadata = TrailMetadataModel.find_by_id(id)
        if metadata:
            return metadata.json(), 200
        return {'message': 'Trail metadata not found'}, 404
    
    def post(self, id):
        if TrailMetadataModel.find_by_id(id):
            return {'message': 'A trail with this Id already exists.'}
        
        data = TrailMetadata.parser.parse_args()
        trail_metadata = TrailMetadataModel(data)

        try:
            trail_metadata.upsert()
        except:
            return {'message': 'An error occurred while uploading trail metadata.'}, 500
        
        return trail_metadata.json(), 201

    def put(self,id):
        if TrailMetadataModel.find_by_id(id):
            data = TrailMetadata.parser.parse_args()
            trail_metadata = TrailMetadataModel(data)
            try:
                trail_metadata.upsert()
            except:
                return {'message': 'An error occurred updating trail metadata.'}, 500
        return {'message': 'A trail with the provided Id does not exist.'}
    
    def delete(self,id):
        trail_metadata = TrailMetadataModel.find_by_id(id)
        if trail_metadata:
            trail_metadata.delete()
            return {'message': 'Trail metadata deleted.'}
        return {'message': 'Trail with the associated id does not exist.'}, 404
