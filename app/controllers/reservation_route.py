from flask import jsonify, abort
from flask_jwt_extended import get_jwt_identity
from flask_restful import Resource, reqparse

from app import db
from app.models.reservation import Reservation
from app.models.show import Show
from app.models.seat import Seat
from app.controllers import reservation_detail_schema, auth_required


class ReservationRoute(Resource):
    @auth_required
    def get(self):
        """get all user reservations"""

        user_id = get_jwt_identity()

        reservations = Reservation.query.filter(Reservation.user_id == user_id).all()
        return jsonify(reservation_detail_schema.dump(reservations, many=True))

    @auth_required
    def post(self):
        """adds Reservations given show and seat ids"""

        parser = reqparse.RequestParser()
        parser.add_argument('show_id', type=int, required=True)
        parser.add_argument('seat_id', action='append', type=int)
        parsed_args = parser.parse_args()
        show_id = parsed_args['show_id']
        seat_ids = parsed_args['seat_id']  # returns list for all args with this key

        existing_show = Show.query.get(show_id)
        if not existing_show:
            return abort(404, 'Show with id: {} does not exist.'.format(show_id))

        seat_reserved_id = self.verifySeatAvailability(seat_ids, show_id)
        if seat_reserved_id:
            return abort(400, 'Selected seats no longer available.')

        for seat_id in seat_ids:
            seat = Seat.query.get(seat_id)
            reservation = Reservation(
                seat_id=seat.id,
                show_id=existing_show.id,
                auditorium_id=existing_show.auditorium_id,
                user_id=get_jwt_identity()
                # user_id = current_user.id
            )

            try:
                # sqlalchemy infers type of arg to decide table for record
                db.session.add(reservation)
                db.session.commit()
            except:
                return abort(500, 'An error occurred while trying to add reservation to database.')

        return jsonify(message='Reservations successfully booked.')

    @auth_required
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('reservation_id', type=int, required=True)
        parsed_args = parser.parse_args()
        res_id = parsed_args['reservation_id']

        user_id = get_jwt_identity()

        #  filter both conditions to check if user is the one making the request
        Reservation.query.filter(Reservation.user_id == user_id, Reservation.id == res_id).delete()

        try:
            db.session.commit()
        except:
            return abort(500, 'An error occurred while trying to delete reservation from database.')

        return jsonify(message='reservation successfully removed.')

    @classmethod
    def verifySeatAvailability(self, seat_ids, show_id):
        for seat_id in seat_ids:
            reservation = Reservation.query.filter(Reservation.seat_id == seat_id, Reservation.show_id == show_id).first()

            if reservation is not None:
                return seat_id
