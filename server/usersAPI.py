from flask import Blueprint, jsonify, request, session, redirect, escape
from sql_alchemy_db_instance import db
from models import Users, Images, LikedImages
from hashutils import make_pw_hash, check_pw_hash
import random


users_api = Blueprint('users_api', __name__)


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

@users_api.route("/logout", methods=["GET"])
def logout():
        del session['user']
        return jsonify(success=True)


@users_api.route('/checksession', methods=["GET"])
def check_session():
        if 'user' in session:
                return jsonify(
                        session = True,
                        user = session['user']
                )
        else:
                return jsonify(session = False)

@users_api.route('/addimage', methods=['POST', 'GET'])
def add_image():
        link = request.json["link"]
        user_id = request.json["user_id"]
        new_image = Images(link=link,user_id=user_id)
        db.session.add(new_image)
        db.session.commit()
        return jsonify(success=True)

@users_api.route('/random-image', methods=['GET'])
def get_random_image():
        image = random.choice(Images.query.all())
        return jsonify(image_link = image.link)

@users_api.route('/like-image', methods=['POST'])
def like_image():
        image_link = request.json['image_link']
        user_id = request.json['user_id']
        # TODO Add in functionality to query LikedImages db to see if that entry already exists
        new_like = LikedImages(image_link=image_link, user_id=user_id)
        db.session.add(new_like)
        db.session.commit()
        return(jsonify(success=True))

@users_api.route('/dislike-image', methods=['POST'])
def dislike_image():
        image_link = request.json['image_link']
        user_id = request.json['user_id']
        # TODO Add in functionality to query LikedImages db to see if that entry already exists
        like_to_delete = LikedImages.query.filter_by(image_link=image_link, user_id=user_id).first()
        db.session.delete(like_to_delete)
        db.session.commit()
        return(jsonify(success=True))

@users_api.route('/all-my-images', methods=['POST'])
def get_all_added_images():
        user_id = request.json['user_id']
        images = Images.query.filter_by(user_id=user_id).all()
        image_links = [image.link for image in images]
        return jsonify(images=image_links)


@users_api.route('/my-liked-images', methods=['POST'])
def get_all_liked_images():
        user_id = request.json['user_id']
        images = LikedImages.query.filter_by(user_id=user_id).all()
        image_links = [image.image_link for image in images]
        return jsonify(images=image_links)
        

# Will use this route later to hide the client ID
@users_api.route('/add-to-imgur', methods=['POST'])
def add_to_imgur():
        return jsonify(client_id = 'aeebe6e47294974')
