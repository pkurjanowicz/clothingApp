from flask import Blueprint, jsonify, request, session, redirect, escape
from sql_alchemy_db_instance import db
from models import Users
from hashutils import make_pw_hash, check_pw_hash


users_api = Blueprint('users_api', __name__)


@users_api.route('/adduser', methods=['POST'])
def add_user():
        username = request.json["username"]
        password = request.json["password"]
        new_user = Users(username=username,password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(success=True)


@users_api.route('/checklogin', methods=['POST'])
def check_user():
        session['user'] = ''
        username = request.json["username"]
        password = request.json["password"]
        user = Users.query.filter_by(username=username).first()
        if check_pw_hash(password, user.pw_hash):
                session['user'] = user.username
                usernamesession = session['user']
                return jsonify(session=usernamesession) #this is for use with the flask module "session"

@users_api.route("/logout", methods=["GET"])
def logout():
        del session['user']
        return jsonify(success=True)


@users_api.route('/checksession', methods=["GET"])
def check_session():
        if 'user' in session:
                print("True")
                return "True"
        else:
                print('false')
                return "False"


