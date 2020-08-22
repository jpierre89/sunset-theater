from app import db
from app.models.roles_users import roles_users
from flask_security import UserMixin


class User(db.Model, UserMixin):
    """a user of this api"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(255), nullable=True)
    active = db.Column(db.Boolean(), nullable=False)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    reservations = db.relationship('Reservation', backref=db.backref('user', lazy=True))

    def __str__(self):
        return self.email

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
