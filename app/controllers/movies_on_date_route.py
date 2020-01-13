from flask import jsonify, abort
from flask_restful import Resource, reqparse

from app.models.show import Show
from app.controllers import movies_on_date_schema, auth_required


class MoviesOnDateRoute(Resource):
    @auth_required
    def get(self):
        """returns movies given a date"""

        parser = reqparse.RequestParser()
        parser.add_argument('date', type=str, required=True)
        parsed_args = parser.parse_args()
        date_arg = parsed_args['date']

        shows = Show.query.filter(Show.date == date_arg).all()

        movies = []
        for show in shows:
            if show.movie not in movies:
                movies.append(show.movie)

        if not movies:
            return abort(404, 'No movies on date')

        return jsonify(movies_on_date_schema.dump(movies, many=True))
