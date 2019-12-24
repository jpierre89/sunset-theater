from application import db
from marshmallow_sqlalchemy import ModelSchema

movies_actors_association = db.Table('actors',
                                     db.Column('actor_id', db.Integer, db.ForeignKey('actor.id'), primary_key=True),
                                     db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True)
                                     )


class Movie(db.Model):
    """a movie for the theater"""

    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    genre = db.relationship('Genre', backref=db.backref('movie', lazy=True))
    cast = db.relationship('Actor', secondary=movies_actors_association, lazy=True,
                           backref=db.backref('movies', lazy=True))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'), nullable=False)
    shows = db.relationship('Show', backref=db.backref('movie', lazy=True))
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.String(255), nullable=False)
    runtime = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return self.title


class Genre(db.Model):
    """a genre for a movie"""

    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Actor(db.Model):
    """an actor in a movie"""

    __tablename__ = 'actor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Director(db.Model):
    """a director or movies"""

    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = name = db.Column(db.String(100), unique=True, nullable=False)
    movies = db.relationship('Movie', backref='director', lazy='dynamic')

    def __repr__(self):
        return self.name


# flask marshmallow serializer
#class MovieSchema(ModelSchema):
#    class Meta:
#        model = Movie


# db.create_all()

#movies_schema = MovieSchema(many=True)
#movie_schema = MovieSchema()
