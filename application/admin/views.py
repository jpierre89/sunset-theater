from .admin import *

# admin views
secure = False  # use to switch between secure view and unsecure view if developing

if secure:
    admin.add_views(
        SecureModelView(Movie, db.session),
        SecureModelView(Director, db.session),
        SecureModelView(Actor, db.session),
        SecureModelView(Genre, db.session),
        SecureModelView(Auditorium, db.session),
        SecureModelView(Row, db.session),
        SecureModelView(Seat, db.session),
        SecureModelView(Show, db.session),
        SecureModelView(Reservation, db.session),
        SecureModelView(User, db.session),
        SecureModelView(Role, db.session)
    )
else:
    admin.add_views(
        ModelView(Movie, db.session),
        ModelView(Director, db.session),
        ModelView(Actor, db.session),
        ModelView(Genre, db.session),
        ModelView(Auditorium, db.session),
        ModelView(Row, db.session),
        ModelView(Seat, db.session),
        ModelView(Show, db.session),
        ModelView(Reservation, db.session),
        ModelView(User, db.session),
        ModelView(Role, db.session)
    )