from flask import Flask

app = Flask(__name__)

def create_app():
    from .home import home_blueprint
    app.register_blueprint(home_blueprint)

    from .datapack_index import index_blueprint
    app.register_blueprint(index_blueprint)

    return app
