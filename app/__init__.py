from flask import Flask
from config import Config
from .orm import db
from flask_migrate import Migrate
from flask_restful import Api
from flask_apispec.extension import FlaskApiSpec

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from .models.users import Users

migrate = Migrate(app, db)

api = Api(app)
docs = FlaskApiSpec(app)
