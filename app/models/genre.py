from app import db


class Genre(db.Model):
    """a genre for a movie"""

    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return self.name
