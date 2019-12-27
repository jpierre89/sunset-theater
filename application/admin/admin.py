from application import app, db
from flask import url_for, redirect, request, abort
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from application.movies import *
from application.theater.models import *
from application.accounts import User, Role

from flask_security import Security, SQLAlchemyUserDatastore
from flask_admin import helpers as admin_helpers

# Flask Admin
admin = Admin(app, name='movielog', base_template='my_master.html', template_mode='bootstrap3')

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
















