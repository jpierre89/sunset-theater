from app import db
from app.models.movies_actors import movies_actors_association


class Movie(db.Model):
    """a movie for the theater"""

    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    genre = db.relationship('Genre', backref=db.backref('movie', lazy=True))
    actors = db.relationship('Actor', secondary=movies_actors_association, lazy=True,
                             backref=db.backref('movies', lazy=True))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.String(255), nullable=False)
    runtime = db.Column(db.Time, nullable=False)
    shows = db.relationship('Show', backref=db.backref('movie', lazy=True))

    def __repr__(self):
        return self.title
