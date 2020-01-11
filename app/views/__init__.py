from flask import redirect, url_for, request, abort
from flask_security import current_user, SQLAlchemyUserDatastore, Security
from flask_admin.contrib.sqla import ModelView
from flask_admin import helpers as admin_helpers, Admin

from app import db, app

# database models
from app.models.auditorium import Auditorium
from app.models.seat import Seat
from app.models.show import Show
from app.models.reservation import Reservation
from app.models.movie import Movie
from app.models.genre import Genre
from app.models.actor import Actor
from app.models.director import Director
from app.models.role import Role
from app.models.user import User


class UnsecureModelView(ModelView):
    """shared configuration options for all admin views"""

    pass


# custom modelview for Flask-Security
class SecureModelView(UnsecureModelView):
    """shared configuration options for secure admin views"""

    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('superuser')
                )

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


class SecureMovieView(SecureModelView):
    """movie view config"""

    form_choices = {
        'rating': [
            ('G', 'G'),
            ('PG', 'PG'),
            ('PG13', 'PG13'),
            ('R', 'R'),
            ('NC17', 'NC17')
        ]
    }


class UnsecureMovieView(UnsecureModelView):
    """movie view config"""

    form_choices = {
        'rating': [
            ('G', 'G'),
            ('PG', 'PG'),
            ('PG13', 'PG13'),
            ('R', 'R'),
            ('NC17', 'NC17')
        ]
    }


# Flask Admin
admin = Admin(app, name='Sunset Theater', base_template='my_master.html', template_mode='bootstrap3')

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )


# admin views
secure = False  # use to switch between secure view and unsecure view if developing

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
        UnsecureMovieView(Movie, db.session, category="Movies"),
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
