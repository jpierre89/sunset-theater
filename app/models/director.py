from app import db


class Director(db.Model):
    """a director or movies"""

    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = name = db.Column(db.String(100), unique=True, nullable=False)
    movies = db.relationship('Movie', backref='director', lazy='dynamic')

    def __repr__(self):
        return self.name
