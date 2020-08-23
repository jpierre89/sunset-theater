import os
from functools import wraps
from flask import render_template, abort, send_from_directory
from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, verify_jwt_in_request
from flask_migrate import Migrate


app = Flask(
    __name__,
    template_folder='./templates',
    static_folder='./static'
)

# Config
app.config.production = False
app.config.development = False
environment = os.getenv("ENVIRONMENT", "development")

if environment == "development":
    from config import DevelopmentConfig
    app.config.from_object(DevelopmentConfig())
    app.config.development = True
    print(f"Theater started with environment = {environment}")
elif environment == "production":
    from config import ProductionConfig
    app.config.from_object(ProductionConfig())
    app.config.production = True
    print(f"Theater started with environment = {environment}")
else:
    raise ValueError(f'"{environment}" not valid environment.')


# Extensions
CORS(app)
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

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

# admin setup and views
from app import views

# route controllers
from app.controllers.api_login_route import ApiLoginRoute
from app.controllers.token_refresh import TokenRefresh
from app.controllers.registration_route import RegistrationRoute
from app.controllers.movie_route import MovieRoute
from app.controllers.movie_list_route import MovieListRoute
from app.controllers.dates_route import DatesRoute
from app.controllers.dates_with_shows_route import DatesWithShowsRoute
from app.controllers.movies_on_date_route import MoviesOnDateRoute
from app.controllers.shows_on_date_route import ShowsOnDateRoute
from app.controllers.show_seating_route import ShowSeatingRoute
from app.controllers.seat_reserved_route import SeatReservedRoute
from app.controllers.reservation_route import ReservationRoute

# add route controllers to routes
base_uri = '/api'

api.add_resource(ApiLoginRoute, base_uri + '/access')
api.add_resource(DatesRoute, base_uri + '/dates')
api.add_resource(MovieRoute, base_uri + '/movie')
api.add_resource(MovieListRoute, base_uri + '/movies/all')
api.add_resource(MoviesOnDateRoute, base_uri + '/movies/date')
api.add_resource(ShowsOnDateRoute, base_uri + '/shows/date')
api.add_resource(ShowSeatingRoute, base_uri + '/show/seating')
api.add_resource(ReservationRoute, base_uri + '/reservations')
api.add_resource(SeatReservedRoute, base_uri + '/seat/reserved')
api.add_resource(RegistrationRoute, base_uri + '/registration')

'''
@app.route('/')
def index():
    return render_template('index.html')  # renders parameter in templates folder
'''

db.create_all()

# populate database and add the admin
from populate import populate
with app.app_context():
    populate(db)

