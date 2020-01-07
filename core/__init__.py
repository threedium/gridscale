# !/usr/bin/env python

# from flask_api import FlaskAPI
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        # create all tables
        db.create_all()

    from .products import prod as products_blueprint
    app.register_blueprint(products_blueprint)

    from .customer import cust as customers_blueprint
    app.register_blueprint(customers_blueprint)

    from .order import ordered as orders_blueprint
    app.register_blueprint(orders_blueprint)

    from .price import price as price_blueprint
    app.register_blueprint(price_blueprint)

    return app
