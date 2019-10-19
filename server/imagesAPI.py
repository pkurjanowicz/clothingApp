from flask import Blueprint, jsonify, request, session, redirect, escape
from sql_alchemy_db_instance import db
from models import Users, Images, LikedImages
import random

#allows me to use images_api as the blueprint for app
images_api = Blueprint('images_api', __name__)

#adds images to db
@images_api.route('/addimage', methods=['POST', 'GET'])
def add_image():
        link = request.json["link"]
        user_id = request.json["user_id"]
        new_image = Images(link=link,user_id=user_id)
        db.session.add(new_image)
        db.session.commit()
        return jsonify(success=True)

#gets a random image
@images_api.route('/random-image', methods=['GET'])
def get_random_image():
        image = random.choice(Images.query.all())
        return jsonify(image_link = image.link)

#adds a liked image to db
@images_api.route('/like-image', methods=['POST'])
def like_image():
        image_link = request.json['image_link']
        user_id = request.json['user_id']
        # TODO Add in functionality to query LikedImages db to see if that entry already exists
        new_like = LikedImages(image_link=image_link, user_id=user_id)
        db.session.add(new_like)
        db.session.commit()
        return(jsonify(success=True))

#deletes the liked image if it exists in db
@images_api.route('/dislike-image', methods=['POST'])
def dislike_image():
        image_link = request.json['image_link']
        user_id = request.json['user_id']
        # TODO Add in functionality to query LikedImages db to see if that entry already exists
        like_to_delete = LikedImages.query.filter_by(image_link=image_link, user_id=user_id).first()
        db.session.delete(like_to_delete)
        db.session.commit()
        return(jsonify(success=True))

#gets all the users uploaded images
@images_api.route('/all-my-images', methods=['POST'])
def get_all_added_images():
        user_id = request.json['user_id']
        images = Images.query.filter_by(user_id=user_id).all()
        image_links = [image.link for image in images]
        return jsonify(images=image_links)

#gets all the users liked images
@images_api.route('/my-liked-images', methods=['POST'])
def get_all_liked_images():
        user_id = request.json['user_id']
        images = LikedImages.query.filter_by(user_id=user_id).all()
        image_links = [image.image_link for image in images]
        return jsonify(images=image_links)
        

# Will use this route later to hide the client ID
@images_api.route('/add-to-imgur', methods=['POST'])
def add_to_imgur():
        return jsonify(client_id = 'aeebe6e47294974')