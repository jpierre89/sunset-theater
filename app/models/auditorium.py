from app import db


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
