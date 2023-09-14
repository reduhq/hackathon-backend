import flaskr.models

from flask import Flask
from config import DevelopmentConfig
from flaskr.extensions import db, migrate, api

from flaskr.resources.user import bp as user_bp


def create_app(testing_config=None):
    app = Flask(__name__)

    if testing_config is None:
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(testing_config)

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    api.init_app(app)

    api.register_blueprint(user_bp, url_prefix="/api")

    return app
