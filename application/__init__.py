from flask import render_template
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)

# provides the settings for the application
app.config.from_object(Config)

api = Api(app)
ma = Marshmallow(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

import application.movies
import application.admin
import application.accounts
import application.access


@app.route('/')
def index():
    return render_template('index.html')  # renders parameter in templates folder
