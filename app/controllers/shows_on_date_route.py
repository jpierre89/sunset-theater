from flask import jsonify, abort
from flask_jwt_extended import jwt_required  # replaced by custom auth_required
from flask_restful import Resource, reqparse
from app.models.show import Show
from app.controllers import shows_movie_nested_schema, auth_required


class ShowsOnDateRoute(Resource):
    @auth_required
    def get(self):
        """returns a list of shows given a date"""

        parser = reqparse.RequestParser()
        parser.add_argument('date', type=str, required=True)
        parsed_args = parser.parse_args()
        date_arg = parsed_args['date']

        shows = Show.query.filter(Show.date == date_arg).all()
        if not shows:
            return abort(404, 'No shows on date')

        return jsonify(shows_movie_nested_schema.dump(shows, many=True))
