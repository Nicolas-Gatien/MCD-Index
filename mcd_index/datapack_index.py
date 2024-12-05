from flask import Blueprint, render_template, request, flash, redirect, current_app, url_for
from werkzeug.utils import secure_filename
import os

index_blueprint = Blueprint("datapack_index", __name__)

def is_archive(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == 'zip'

@index_blueprint.route('/api/get', methods=['POST'])
def get_datapack():
    return "Got Datapack"

@index_blueprint.route('/api/add', methods=['POST'])
def add_datapack():
    print(request.files)

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
    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    return "Uploading Datapack"

@index_blueprint.route('/upload')
def upload_datapack():
    return render_template('upload.html')