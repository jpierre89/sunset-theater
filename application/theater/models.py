from application import db
from application.accounts.models import User
from application.movies.models import Movie
# from marshmallow_sqlalchemy import ModelSchema


class Auditorium(db.Model):
    """an auditorium with a movie screen"""

    __tablename__ = 'auditorium'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    seats = db.relationship('Seat', backref=db.backref('auditorium', lazy=True))
    shows = db.relationship('Show', backref=db.backref('auditorium', lazy=True))
    reservations = db.relationship('Reservation', backref=db.backref('auditorium', lazy=True))

    def __repr__(self):
        return self.name


class Seat(db.Model):
    """a seat in a single row in a single auditorium"""

    __tablename__ = 'seat'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String, nullable=False)
    auditorium_id = db.Column(db.Integer, db.ForeignKey('auditorium.id'), nullable=False)
    reservations = db.relationship('Reservation', backref=db.backref('seat', lazy=True))

    def __repr__(self):
        auditorium = Auditorium.query.get(self.auditorium_id)
        return "{} {}".format(self.number, auditorium.name)


class Show(db.Model):
    """a movie showing in an auditorium"""

    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    auditorium_id = db.Column(db.Integer, db.ForeignKey('auditorium.id'), nullable=False)
    reservations = db.relationship('Reservation', backref=db.backref('show', lazy=True))

    def __repr__(self):
        auditorium = Auditorium.query.get(self.auditorium_id)
        movie = Movie.query.get(self.movie_id)
        return "{} {} {}".format(movie.title, self.start_time, auditorium)


class Reservation(db.Model):
    """a reservation for a single seat by a user"""

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
        return "{} {} {} {} {}".format(movie.title, show.start_time, auditorium.name, seat.number, user.email)




#db.create_all()
