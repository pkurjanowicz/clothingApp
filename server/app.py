import os
from flask import Flask
from sql_alchemy_db_instance import db
from usersAPI import users_api

project_dir = os.path.dirname(os.path.abspath(__file__))
project_paths = project_dir.split("/")
project_paths.pop()
project_paths.append('db')
project_dir = "/".join(project_paths)

def create_app():
    app = Flask(__name__,
        static_folder = "./dist/static",
        template_folder = "./dist"
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, "clothingapp.db"))
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    app.register_blueprint(users_api)
    return app

def setup_database(app):
    with app.app_context():
        db.create_all()