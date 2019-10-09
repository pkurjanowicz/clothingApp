from flask import Blueprint, jsonify, request
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

