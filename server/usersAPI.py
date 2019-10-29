from flask import Blueprint, jsonify, request, session
from sql_alchemy_db_instance import db
from models import Users, Images, LikedImages
from hashutils import make_pw_hash, check_pw_hash

# Allows me to use users_api as a Blueprint for app
users_api = Blueprint('users_api', __name__)

#adds a new user, note there is no server side validation
@users_api.route('/adduser', methods=['POST'])
def add_user():
        username = request.json["username"]
        password = request.json["password"]
        new_user = Users(username=username,password=password)
        db.session.add(new_user)
        db.session.commit()
        user = Users.query.filter_by(username=username).first()
        session['user'] = user.id
        usernamesession = session['user']
        return jsonify(session=usernamesession)

#checks that the user is in db and has the right 
# pass, no catch for in correct user or pass yet...
@users_api.route('/checklogin', methods=['POST'])
def check_user():
        session['user'] = ''
        username = request.json["username"]
        password = request.json["password"]
        user = Users.query.filter_by(username=username).first()
        if check_pw_hash(password, user.pw_hash):
                session['user'] = user.id
                usernamesession = session['user']
                return jsonify(session=usernamesession) #this is used to pass session to vue

#deletes user session, this will redirect them back to login
@users_api.route("/logout", methods=["GET"])
def logout():
        del session['user']
        return jsonify(success=True)

#helper route to check if the user is in session
@users_api.route('/checksession', methods=["GET"])
def check_session():
        if 'user' in session:
                return jsonify(
                        session = True,
                        user = session['user']
                )
        else:
                return jsonify(session = False)

@users_api.route('/submitProfileData', methods=['POST'])
def submit_profile_data():
        timezone = request.json["timezone"]
        current_user = request.json["currentuser"]
        user = Users.query.filter_by(id=current_user).first()
        user.time_zone = timezone
        db.session.commit()
        return jsonify(success=True, user_time=timezone)

@users_api.route('/getProfileData', methods=['POST'])
def get_profile_data():
        current_user = request.json["currentuser"]
        user = Users.query.filter_by(id=current_user).first()
        return jsonify(success=True, user_time=user.time_zone)
