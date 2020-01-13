from flask import jsonify
from flask_restful import Resource, reqparse

from app.controllers import auth_required
from app.models.reservation import Reservation


class SeatReservedRoute(Resource):
    """returns true if a seat is reserved for a show; else false"""
    @auth_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('show_id', type=int, required=True)
        parser.add_argument('seat_id', type=int, required=True)
        parsed_args = parser.parse_args()
        seat_id = parsed_args['seat_id']
        show_id = parsed_args['show_id']

        is_reserved = True
        reservation = Reservation.query.filter(Reservation.seat_id == seat_id, Reservation.show_id == show_id).first()

        if reservation is None:
            is_reserved = False

        return jsonify(is_reserved)