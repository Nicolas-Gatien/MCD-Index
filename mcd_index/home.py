from flask import Blueprint, render_template
from . import Datapack, db

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/")
def index():
    datapacks = db.session.execute(db.select(Datapack).order_by(Datapack.idname)).scalars().all()
    return render_template('home.html', datapacks=datapacks)