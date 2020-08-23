from flask import jsonify, abort
from flask_restful import Resource, reqparse
from app.models.show import Show
from app.models.auditorium import Auditorium
from app.controllers import seating_schema, auth_required
from app.controllers.reservation_route import ReservationRoute
from flask_jwt_extended import get_jwt_identity


class ShowSeatingRoute(Resource):
    """returns a sorted list of all seats for a show given a show id"""

    @auth_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('show_id', type=int, required=True)
        parsed_args = parser.parse_args()
        show_id = parsed_args['show_id']

        show = Show.query.get(show_id)
        if not show:
            return abort(404, 'Show with id: {} does not exist in database.'.format(show_id))

        auditorium = Auditorium.query.get(show.auditorium_id)
        auditorium_seats = auditorium.seats
        if not auditorium_seats:
            return abort(404, 'Auditorium Error.')

        auditorium_seats = sorted(
            # x.number.length is < 3
            auditorium_seats, key=lambda x: (x.number[0], int(x.number[1:])), reverse=False
        )
        
        seats = seating_schema.dump(auditorium_seats, many=True)
        
        for seat in seats:
            reserved_id = ReservationRoute.verifySeatAvailability([seat["id"],], show_id)
            if reserved_id:
                seat["is_reserved"] = True
            else:
                seat["is_reserved"] = False

        return jsonify(seats)
