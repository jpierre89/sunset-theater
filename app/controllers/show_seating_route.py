from flask import jsonify, abort
from flask_restful import Resource, reqparse
from app.models.show import Show
from app.models.auditorium import Auditorium
from app.controllers import seating_schema, auth_required


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

        auditorium_seats = sorted(auditorium_seats, key=lambda x: x.number, reverse=False)
        return jsonify(seating_schema.dump(auditorium_seats, many=True))
