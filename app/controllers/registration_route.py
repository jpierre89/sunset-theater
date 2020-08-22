import datetime
from flask import jsonify, abort
from flask_restful import Resource, reqparse
from app import db
from app.models.user import User


class RegistrationRoute(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('first_name', type=str, required=False)
        parsed_args = parser.parse_args()
        username = parsed_args['username']
        password = parsed_args['password']
        first = parsed_args.get('first_name', None)

        existing_user = User.query.filter(User.username == username).first()
        if existing_user:
            return abort(401, 'username already exists')

        user = User(
            username=username,
            password=password,
            active=True,
            confirmed_at=datetime.datetime.now()
        )
        if first:
            user.first_name = first

        try:
            db.session.add(user)
            db.session.commit()
        except:
            return abort(500, 'An error occurred while trying to add reservation to database.')

        return jsonify(message='User registered')
