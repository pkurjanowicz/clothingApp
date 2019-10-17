from flask import Flask, render_template, session, redirect,request, abort,jsonify
from app import create_app, setup_database
from models import Users
from hashutils import make_pw_hash, check_pw_hash

def add_vue_routes(app):

    @app.route('/', defaults={'path': ''})

    @app.route('/<path:path>')
    def catch_all(path):
        return render_template("index.html")


    @app.after_request
    def add_header(req):
        """
        Clear Cache for hot-reloading
        """
        req.headers["Cache-Control"] = "no-cache"
        return req
    
    # @app.before_request
    # def require_login():
    #     if not ('user' in session):
    #         session['user'] = ''
    #         return redirect('/login')
    



if __name__ == "__main__":
    app = create_app()
    add_vue_routes(app)
    setup_database(app)
    app.run(debug=True)


