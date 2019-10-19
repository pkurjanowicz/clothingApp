import os
from flask import Flask, session, current_app
from sql_alchemy_db_instance import db
from usersAPI import users_api
from imagesAPI import images_api
from secrets import secret_key

# creats the correct path for the db file
project_dir = os.path.dirname(os.path.abspath(__file__))
project_paths = project_dir.split("/")
project_paths.pop()
project_paths.append('db')
project_dir = "/".join(project_paths)

# creates app, registers blueprint, and 
# returns the app for use in the main.py file
def create_app():
    app = Flask(__name__,
        static_folder = "./dist/static",
        template_folder = "./dist"
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, "clothingapp.db"))
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    app.register_blueprint(users_api)
    app.register_blueprint(images_api)
    app.secret_key = secret_key
    return app

# this actually keeps db refreshed if new tables are added
def setup_database(app):
    with app.app_context():
        db.create_all()