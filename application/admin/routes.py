from .models import *

# admin views
secure = True  # use to switch between secure view and unsecure view if developing

if secure:
    admin.add_views(
        SecureMovieView(Movie, db.session, category="Movies"),
        SecureModelView(Director, db.session, category="Movies"),
        SecureModelView(Actor, db.session, category="Movies"),
        SecureModelView(Genre, db.session, category="Movies")
    )
    admin.add_views(
        SecureModelView(Auditorium, db.session, category="Theater"),
        SecureModelView(Seat, db.session, category="Theater"),
    )
    admin.add_views(
        SecureModelView(Show, db.session, category="booking"),
        SecureModelView(Reservation, db.session, category="booking"),
    )
    admin.add_views(
        SecureModelView(User, db.session, category="Accounts"),
        SecureModelView(Role, db.session, category="Accounts")
    )
else:
    admin.add_views(
        UnsecureModelView(Movie, db.session, category="Movies"),
        UnsecureModelView(Director, db.session, category="Movies"),
        UnsecureModelView(Actor, db.session, category="Movies"),
        UnsecureModelView(Genre, db.session, category="Movies")
    )
    admin.add_views(
        UnsecureModelView(Auditorium, db.session, category="Theater"),
        UnsecureModelView(Seat, db.session, category="Theater")
    )
    admin.add_views(
        UnsecureModelView(Show, db.session, category="booking"),
        UnsecureModelView(Reservation, db.session, category="booking")
    )
    admin.add_views(
        UnsecureModelView(User, db.session, category="Accounts"),
        UnsecureModelView(Role, db.session, category="Accounts")
    )
