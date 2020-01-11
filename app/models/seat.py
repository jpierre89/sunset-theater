from app import db
from app.models.auditorium import Auditorium


class Seat(db.Model):
    """a seat in a single row in a single auditorium"""

    __tablename__ = 'seat'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String, nullable=False)
    row = db.Column(db.String, nullable=True)  # change
    auditorium_id = db.Column(db.Integer, db.ForeignKey('auditorium.id'), nullable=False)
    is_empty_space = db.Column(db.Boolean)  # TODO makes checks for empty on routes
    reservations = db.relationship('Reservation', backref=db.backref('seat', lazy=True))

    def __repr__(self):
        auditorium = Auditorium.query.get(self.auditorium_id)
        return "{}{} {}".format(self.row, self.number, auditorium.name)
