from flask import Flask

app = Flask(__name__)

def create_app():
    from .index import index_bp
    app.register_blueprint(index_bp)

    return app
