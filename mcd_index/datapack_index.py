from flask import Blueprint, render_template

index_blueprint = Blueprint("datapack_index", __name__)

@index_blueprint.route('/api/get', methods=['POST'])
def get_datapack():
    return "Got Datapack"

@index_blueprint.route('/api/add', methods=['POST'])
def add_datapack():
    return "Uploading Datapack"

@index_blueprint.route('/upload')
def upload_datapack():
    return render_template('upload.html')