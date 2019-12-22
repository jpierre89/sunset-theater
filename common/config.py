import os
basedir = os.path.abspath(os.path.dirname(__file__))


# stores configuration variables
class Config(object):
    # Create Database and SQL Alchemy settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + 'api.db'
    SQLALCHEMY_ECHO = True
    # signals app every time change is about to be made to database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # key for sessions
    # Flask and some extensions use this var to generate tokens or signatures
    # Can set a secure password in environment variable so not known through this file
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'password!'

    # Basic Auth Settings
    BASIC_AUTH_USERNAME = 'txstate'
    BASIC_AUTH_PASSWORD = 'txstate'
    BASIC_AUTH_FORCE = True  # makes the user/password site wide.

    # Flask Admin settings
    FLASK_ADMIN_SWATCH = 'cerulean'

    # Flask Security settings
    SECURITY_URL_PREFIX = '/admin'
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = 'IIUHF0asdfkl98VHGlasdkl'
    SECURITY_LOGIN_URL = '/login/'
    SECURITY_LOGOUT_URL = '/logout/'
    SECURITY_REGISTER_URL = '/register/'
    SECURITY_POST_LOGIN_VIEW = '/admin/'
    SECURITY_POST_LOGOUT_VIEW = '/admin/'
    SECURITY_POST_REGISTER_VIEW = '/admin/'
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False

    # JWT settings
    JWT_SECRET_KEY = 'SECRET'
