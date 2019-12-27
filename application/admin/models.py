from .admin import *


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
