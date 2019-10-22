from flask import Blueprint, jsonify, request, session, redirect, escape
from sql_alchemy_db_instance import db
from models import Users, Images, LikedImages
import random
import time

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

#gets a random image, this only returns 
# other user's images, not the user logged in's images
@images_api.route('/random-image', methods=['GET', 'POST'])
def get_random_image():
        user_id = request.json['user_id']
        id_list_object = Images.query.all()
        id_list = [value.user_id for value in id_list_object]
        new_list = list(filter(lambda a: a != user_id, id_list))
        user_id = random.choice(new_list)
        images = Images.query.filter_by(user_id=user_id).all()
        image_link_list = [image.link for image in images]
        return jsonify(image_link = random.choice(image_link_list))

#adds a liked image to db
@images_api.route('/like-image', methods=['POST'])
def like_image():
        image_link = request.json['image_link']
        user_id = request.json['user_id']
        owner_id = Images.query.filter_by(link=image_link).first().user_id
        # TODO Add in functionality to query LikedImages db to see if that entry already exists
        new_like = LikedImages(image_link=image_link, user_id=user_id, owner_id=owner_id)
        db.session.add(new_like)
        db.session.commit()
        # time.sleep(5)
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
@images_api.route('/find-match', methods=['POST'])
def find_match():
        liker_id = request.json['liker_id']
        image_link = request.json['image_link']
        image_owner_id = LikedImages.query.filter_by(image_link=image_link).first()
        if not image_owner_id:
                return jsonify(match=False)
        image_owner_id = image_owner_id.owner_id
        owner_liked_liker_image = LikedImages.query.filter_by(owner_id=liker_id, user_id=image_owner_id).first().owner_id
        if owner_liked_liker_image != '':
                return jsonify(match=True, liked_image=owner_liked_liker_image)
        return jsonify(match=False)
        

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