# coding = utf-8
"""
@author: zhou
@time:2019/1/15 11:14
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_cors import CORS

db = SQLAlchemy()
cors = CORS()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    cors.init_app(app, supports_credentials=True)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .api_1_0 import api_1_0 as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
