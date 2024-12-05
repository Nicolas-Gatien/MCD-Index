from flask import Blueprint, render_template, request, flash, redirect, current_app, url_for
from werkzeug.utils import secure_filename
import os

from . import Datapack, db

index_blueprint = Blueprint("datapack_index", __name__)

def is_archive(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == 'zip'

@index_blueprint.route('/api/get', methods=['GET'])
def get_datapack():
    return "Get Datapack"

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
    print(f"{datapack_name}: {datapack_path}")
    file.save(datapack_path)
    datapack: Datapack = Datapack(
        name=datapack_name,
        path=datapack_path
    )
    db.session.add(datapack)
    db.session.commit()
    return "Uploading Datapack"

@index_blueprint.route('/upload')
def upload_datapack():
    return render_template('upload.html')

@index_blueprint.route('/list')
def list_datapacks():
    datapacks = db.session.execute(db.select(Datapack).order_by(Datapack.name)).scalars().all()
    return render_template('list.html', datapacks=datapacks)