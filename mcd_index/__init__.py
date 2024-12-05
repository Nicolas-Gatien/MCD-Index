from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

import os
from dotenv import load_dotenv

if os.path.isfile('.env'):
    load_dotenv()
else:
    print("Using Server Env")

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["UPLOAD_FOLDER"] = '/datapacks'
app.secret_key = os.getenv("APP_SECRET_KEY")
db = SQLAlchemy(model_class=Base)

class Datapack(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    path: Mapped[str] = mapped_column(unique=True)

def create_app():
    from .home import home_blueprint
    app.register_blueprint(home_blueprint)

    from .datapack_index import index_blueprint
    app.register_blueprint(index_blueprint)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
