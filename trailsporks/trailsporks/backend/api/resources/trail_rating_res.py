from flask_restful import Resource, reqparse
from models.trail_rating import TrailRatingModel


class TrailRating(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "rating",
        type=str,
        required=True,
        help="Rating of Trail Difficulty. Examples: Green, Blue, Black, Double Black",
    )

    def get(self, rating):
        rating = TrailRatingModel.find_by_rating(rating)
        if rating:
            print(rating)
            return rating.json()
        return {"message": "rating not found"}, 404

    def post(self, rating):
        if TrailRatingModel.find_by_rating(rating):
            return {"message": "The rating already exists"}, 400

        rating = TrailRatingModel.find_by_rating(rating)

        try:
            rating.upsert()
        except:
            return {"message": "An error occurred uploading the rating."}, 500

    def put(self, rating):
        if TrailRatingModel.find_by_rating(rating):
            rating = TrailRatingModel
            try:
                rating.upsert()
            except Exception as e:
                print(e)
                return {"message": "An error occurred uploading the rating."}, 500
        return {"message": "The provided rating does not exist."}

    def delete(self, name):
        rating = TrailRatingModel.find_by_rating(rating)
        if rating:
            rating.delete()
            return {"message": "Rating deleted."}
        return {"message": "The provided rating does not exist."}, 404
