from flask import Blueprint

index_blueprint = Blueprint("datapack_index", __name__)

@index_blueprint.route('/get')
def get_datapack():
    return "Got Datapack"