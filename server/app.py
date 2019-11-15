import os
from flask import Flask, session, current_app
from sql_alchemy_db_instance import db
from usersAPI import users_api
from imagesAPI import images_api
from messagesAPI import messages_api


secret_key1 = 'X!Cfzp6GfFYeFg.pgUxanVRi2!'
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

    if os.environ["RUN_ENVIRONMENT"] == 'network':
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(user=os.environ["DB_USER"],pw=os.environ["DB_PASS"],url=os.environ["DB_URL"],db=os.environ["DB_NAME"])
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, "clothingapp.db"))
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    app.register_blueprint(users_api)
    app.register_blueprint(images_api)
    app.register_blueprint(messages_api)
    try:
        from secrets import secret_key
        app.secret_key = secret_key
    except ImportError:
        app.secret_key = secret_key1
    return app

# this actually keeps db refreshed if new tables are added
def setup_database(app):
    with app.app_context():
        db.create_all()
