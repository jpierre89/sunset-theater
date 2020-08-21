import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig():
    """Abstract"""

    FLASK_ADMIN_SWATCH = 'cerulean'
    # Flask Security non-private settings
    SECURITY_URL_PREFIX = '/admin'
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_LOGIN_URL = '/login/'
    SECURITY_LOGOUT_URL = '/logout/'
    SECURITY_REGISTER_URL = '/register/'
    SECURITY_POST_LOGIN_VIEW = '/admin/'
    SECURITY_POST_LOGOUT_VIEW = '/admin/'
    SECURITY_POST_REGISTER_VIEW = '/admin/'
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')

    # key for sessions, Flask and some extensions
    SECRET_KEY = 'password'

    # JWT settings
    JWT_SECRET_KEY = 'SECRET'


class ProductionConfig(BaseConfig):
    FLASK_ADMIN_SWATCH = 'cerulean'
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self):
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        self.JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
        #db
        self.DB_TYPE = os.getenv("DB_TYPE")
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_PORT = os.getenv('DB_PORT')

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        #postgres
        return '{type}://{user}:{pwd}@{host}:{port}/{name}'.format(
            type=self.DB_TYPE, user=self.DB_USER, pwd=self.DB_PASSWORD,
            host=self.DB_HOST, port=self.DB_PORT, name=self.DB_NAME)




