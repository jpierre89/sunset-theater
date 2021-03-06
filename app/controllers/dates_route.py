from flask import jsonify, abort
from flask_restful import Resource, reqparse

from app.controllers import auth_required
from app.models.movie import Movie


class DatesRoute(Resource):
    @auth_required
    def get(self):
        """returns dates a movie is playing given a movie's id"""

        parser = reqparse.RequestParser()
        parser.add_argument('movie_id', type=int, required=True)
        parsed_args = parser.parse_args()
        id_arg = parsed_args['movie_id']

        movie = Movie.query.get(id_arg)
        if not movie:
            return abort(404, 'Movie with id: {} does not exist in database.'.format(id_arg))

        dates = []
        for show in movie.shows:
            if show.date not in dates:
                dates.append(show.date)

        return jsonify(dates)
