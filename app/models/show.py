from app import db
from app.models.auditorium import Auditorium
from app.models.movie import Movie


class Show(db.Model):
    """a movie showing in an auditorium"""

    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Time, nullable=False)
    date = db.Column(db.Date, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    auditorium_id = db.Column(db.Integer, db.ForeignKey('auditorium.id'), nullable=False)
    reservations = db.relationship('Reservation', backref=db.backref('show', lazy=True))

    def __repr__(self):
        auditorium = Auditorium.query.get(self.auditorium_id)
        movie = Movie.query.get(self.movie_id)
        return "{} {} {}".format(movie.title, self.time, auditorium)
