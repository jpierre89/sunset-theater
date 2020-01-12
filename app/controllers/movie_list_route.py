from flask import jsonify, abort
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.models.movie import Movie
from app.controllers import movie_schema, auth_required


class MovieListRoute(Resource):
    @auth_required
    def get(self):
        """returns a list of all movies"""

        movies = Movie.query.all()

        if not movies:
            return abort(404, 'No movies exist')

        return jsonify(movie_schema.dump(movies, many=True))
