from flask import Flask, render_template, session, redirect,request, abort,jsonify
from app import create_app, setup_database
from models import Users
from hashutils import make_pw_hash, check_pw_hash

def add_vue_routes(app):

    # function says default path is home
    @app.route('/', defaults={'path': ''})

    # function allows vue router to designate the 
    # content and just renders index.html no matter what 
    # path is used.
    @app.route('/<path:path>')
    def catch_all(path):
        return render_template("index.html")

    # Clears cache for hot-reloading
    @app.after_request
    def add_header(req):
        req.headers["Cache-Control"] = "no-cache"
        return req
    
app = create_app()
add_vue_routes(app)
setup_database(app)

# Creates the app, database and all the routes
if __name__ == "__main__":
    app.run(debug=True)


