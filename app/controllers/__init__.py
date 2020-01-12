from functools import wraps

from flask_jwt_extended import verify_jwt_in_request

from app import ma, app
from flask import abort
from marshmallow import fields
from marshmallow_sqlalchemy.fields import Nested

from app.models.user import User
from app.models.movie import Movie
from app.models.actor import Actor
from app.models.genre import Genre
from app.models.director import Director
from app.models.show import Show
from app.models.auditorium import Auditorium
from app.models.reservation import Reservation
from app.models.seat import Seat
from app.models.role import Role


def auth_required(func):
    """decorator - require valid/non-expired access token"""

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            verify_jwt_in_request()  # throws error if token expired or not valid
        except:
            app.logger.error('jwt token auth failed: invalid or expired')
            abort(401)

        return func(*args, **kwargs)

    return wrapper


class RoleSchema(ma.ModelSchema):
    class Meta:
        model = Role


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


class ShowSchema(ma.ModelSchema):
    class Meta:
        model = Show


class MovieSchema(ma.ModelSchema):
    class Meta:
        model = Movie


class GenreSchema(ma.ModelSchema):
    class Meta:
        model = Genre


class DirectorSchema(ma.ModelSchema):
    class Meta:
        model = Director


class ActorSchema(ma.ModelSchema):
    class Meta:
        model = Actor


class SeatSchema(ma.ModelSchema):
    class Meta:
        model = Seat


class SeatingSchema(ma.ModelSchema):
    id = fields.Int()
    number = fields.String()
    row = fields.String()
    auditorium_id = fields.Int()
    is_empty_space = fields.Boolean()


class AuditoriumSchema(ma.ModelSchema):
    class Meta:
        model = Auditorium


class ReservationSchema(ma.ModelSchema):
    class Meta:
        model = Reservation


class ShowMovieNestedSchema(ma.ModelSchema):
    """excludes reservations"""

    id = fields.Int()
    time = fields.Time()
    date = fields.Date()
    auditorium_id = fields.Int()
    movie = Nested(MovieSchema, exclude=("shows",))


class ReservationDetailSchema(ma.ModelSchema):
    """nested schemas replace ids"""

    id = fields.Int()
    seat = Nested(SeatSchema, exclude=("reservations",))
    show = Nested(ShowMovieNestedSchema)
    auditorium = Nested(AuditoriumSchema, exclude=("id", "seats", "shows", "reservations"))


class MoviesOnDateSchema(ma.ModelSchema):
    """excludes shows"""

    id = fields.Int()
    title = fields.String()
    description = fields.String()
    rating = fields.String()
    runtime = fields.Time()
    director = Nested(DirectorSchema, exclude=("movies",))
    genre = Nested(GenreSchema, exclude=("movie",))
    actors = Nested(ActorSchema, many=True, exclude=("movies",))


# generic table schemas
movie_schema = MovieSchema()
director_schema = DirectorSchema()
actor_schema = ActorSchema()
genre_schema = GenreSchema()
auditorium_schema = AuditoriumSchema()
seat_schema = SeatSchema()
show_schema = ShowSchema()
reservation_schema = ReservationSchema()
user_schema = UserSchema()
role_schema = RoleSchema()

# special schemas
shows_movie_nested_schema = ShowMovieNestedSchema()
movies_on_date_schema = MoviesOnDateSchema()
reservation_detail_schema = ReservationDetailSchema()
seating_schema = SeatingSchema()








