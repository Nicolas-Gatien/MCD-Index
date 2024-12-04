from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

import os

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
db = SQLAlchemy(model_class=Base)

def create_app():
    from .home import home_blueprint
    app.register_blueprint(home_blueprint)

    from .datapack_index import index_blueprint
    app.register_blueprint(index_blueprint)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URI"]

    db.init_app(app)

    return app
