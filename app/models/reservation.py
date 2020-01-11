from app import db
from app.models.seat import Seat
from app.models.user import User
from app.models.show import Show
from app.models.movie import Movie
from app.models.auditorium import Auditorium


class Reservation(db.Model):
    """reservation for a single show for all seats by a single user"""

    __tablename__ = 'reservation'
    id = db.Column(db.Integer, primary_key=True)
    seat_id = db.Column(db.Integer, db.ForeignKey('seat.id'), nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
    auditorium_id = db.Column(db.Integer, db.ForeignKey('auditorium.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        seat = Seat.query.get(self.seat_id)
        user = User.query.get(self.user_id)
        show = Show.query.get(self.show_id)
        movie = Movie.query.get(show.movie_id)
        auditorium = Auditorium.query.get(self.auditorium_id)
        return "{} {} {} {} {}".format(movie.title, show.time, auditorium.name, seat.number, user.email)
