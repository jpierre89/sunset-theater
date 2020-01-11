import datetime
from flask import jsonify
from flask_restful import Resource, reqparse, abort
from app import db
from app.models.user import User


class RegistrationRoute(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('last_name', type=str, required=True)
        parsed_args = parser.parse_args()
        email = parsed_args['email']
        password = parsed_args['password']
        first = parsed_args['first_name']
        last = parsed_args['last_name']

        existing_user = User.query.filter(User.email == email).first()
        if existing_user:
            return abort(400, 'Email already exists')

        user = User(
            first_name=first,
            last_name=last,
            email=email,
            password=password,
            active=True,
            confirmed_at=datetime.datetime.now()
        )

        try:
            db.session.add(user)
            db.session.commit()
        except:
            return abort(500, 'An error occurred while trying to add reservation to database.')

        return jsonify(message='User registered')
