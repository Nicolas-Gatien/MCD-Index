from flask import Blueprint, render_template, request, flash, redirect, current_app, url_for, send_file
from werkzeug.utils import secure_filename
import os

from . import Datapack, db

index_blueprint = Blueprint("datapack_index", __name__)

def is_archive(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == 'zip'

@index_blueprint.route('/api/get/<string:name>', methods=['GET'])
def get_datapack(name: str):
    datapack: Datapack = Datapack.query.filter_by(idname=name).first()

    path = os.path.join(current_app.config['UPLOAD_FOLDER'], datapack.filename)
    return send_file(os.path.abspath(path), as_attachment=True)

@index_blueprint.route('/api/add', methods=['POST'])
def add_datapack():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('datapack_index.upload_datapack'))
    file = request.files['file']

    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('datapack_index.upload_datapack'))
    
    if not is_archive(file.filename):
        flash('Upload a zipped folder')
        return redirect(url_for('datapack_index.upload_datapack'))
    
    filename = secure_filename(file.filename)
    datapack_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

    datapack_name = request.form['id']
    file.save(datapack_path)
    datapack: Datapack = Datapack(
        idname=datapack_name,
        filename=filename
    )
    db.session.add(datapack)
    db.session.commit()
    return "Uploading Datapack"

@index_blueprint.route('/upload')
def upload_datapack():
    return render_template('upload.html')