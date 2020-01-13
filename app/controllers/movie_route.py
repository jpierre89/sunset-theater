from flask import jsonify, abort
from flask_restful import Resource, reqparse

from app import db
from app.models.movie import Movie
from app.models.actor import Actor
from app.controllers import movie_schema, auth_required


class MovieRoute(Resource):
    @auth_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('movie_id', type=int, required=True)
        parsed_args = parser.parse_args()

        movie = Movie.query.filter(Movie.id == parsed_args['movie_id']).first()
        if not movie:
            return abort(404, 'Movie with id: {} does not exist in database.'.format(parsed_args['movie_id']))

        # return jsonify(movie.title)
        return jsonify(movie_schema.dump(movie))

    @auth_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True),
        parser.add_argument('genre_id', type=int, required=True),
        parser.add_argument('cast_id', action='append', type=str)
        parsed_args = parser.parse_args()

        title = parsed_args['title']
        genre_id = parsed_args['genre_id']

        existing_movie = Movie.query.filter(Movie.title == title).first()
        if existing_movie:
            return abort(400, 'Movie with title: {} already exists in database.'.format(parsed_args['title']))

        movie = Movie(
            title=title,
            genre_id=genre_id
        )

        if self.args['cast_id']:
            for id in self.args['cast_id']:
                actor = Actor.query.filter(Actor.id == id).first()
                if not actor:
                    return abort(404, 'Actor with id: {} does not exist in database.'.format(id))
                movie.cast.append(actor)
                db.session.commit()

        try:
            db.session.add(movie)
            db.session.commit()
        except:
            return abort(500, 'An error occurred while trying to add new movie to database.')

        return jsonify(message='New movie has been created.')
