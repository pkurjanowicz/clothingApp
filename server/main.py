from flask import Flask, render_template, session, redirect,request, abort,jsonify
from app import create_app, setup_database
from models import Users
from hashutils import make_pw_hash, check_pw_hash

def add_vue_routes(app):

    @app.route('/', defaults={'path': ''})

    @app.route('/<path:path>')
    def catch_all(path):
        return render_template("index.html")
    
    # @app.route('/login')
    # def catch_login_redirect():
    #     return render_template('index.html')
    
    @app.route('/checklogin', methods=['POST', 'GET'])
    def check_user():
        if request.method == "POST":
            session['user'] = ''
            username = request.json["username"]
            password = request.json["password"]
            user = Users.query.filter_by(username=username).first()
            if check_pw_hash(password, user.pw_hash):
                session['user'] = True
                return jsonify(session=True)
        else:
            return print('Hello')

    # @app.route('/checksession', methods=["GET"])
    # def check_session():
    #     print(session['user'])
    #     if session.get('user') == True:
    #         return 'True'
    #     return 'False'

    # @app.after_request
    # def add_header(req):
    #     """
    #     Clear Cache for hot-reloading
    #     """
    #     req.headers["Cache-Control"] = "no-cache"
    #     return req
    
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


