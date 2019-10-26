from flask import Blueprint, jsonify, request, session, redirect, escape
from sql_alchemy_db_instance import db
from models import Users, Images, LikedImages, Messages


messages_api = Blueprint('messages_api', __name__)

@messages_api.route('/return_messagable_users', methods=['POST'])
def return_messagable_users():
    current_user_id = request.json["current_user_id"]
    total_user_ids = LikedImages.query.filter_by(user_id=current_user_id).all() #pulls out objects that only current user liked
    total_image_owner_ids = [value.owner_id for value in total_user_ids] #iterates over object list and pulls out the owner IDs of those items
    deduped_total_user_ids = set(total_image_owner_ids)
    list_of_image_owner_ids = list(deduped_total_user_ids)
    image_owner_names = []
    for user_id in list_of_image_owner_ids:
        user_name = Users.query.filter_by(id=user_id).first()
        image_owner_names.append(user_name.username)
    return jsonify(user_list=image_owner_names)

@messages_api.route('/add_message', methods=['POST'])
def add_message():
    first_user_id = request.json["first_user_id"]
    second_user_name = request.json["second_user_name"]
    message = request.json["message"]
    second_user_id = Users.query.filter_by(username=second_user_name).first().id
    new_message = Messages(first_user_id=first_user_id,second_user_id=second_user_id, message=message)
    db.session.add(new_message)
    db.session.commit()
    return jsonify(message=new_message.message)

@messages_api.route('/get_all_messages', methods=['POST'])
def get_all_messages():
    current_user_id = request.json["current_user_id"]
    second_user_name = request.json['second_user_name']
    second_user_id = Users.query.filter_by(username=second_user_name).first().id
    current_user_sent_messages = Messages.query.filter(Messages.first_user_id == current_user_id, Messages.second_user_id == second_user_id).all()
    current_user_recieved_messages = Messages.query.filter(Messages.first_user_id == second_user_id, Messages.second_user_id == current_user_id).all()
    # .filter(User.username=='Bob', Space.name=='Mainspace').first()
    # sent_messages = Messages.query.filter_by(first_user_id=current_user_id).all()
    # recieved_messages = Messages.query.filter_by(second_user_id=second_user_id).all()
    sent_messages = [message.message for message in current_user_sent_messages]
    recieved_messages = [message.message for message in current_user_recieved_messages]
    # total_messages_objects = current_user_sent_messages + current_user_recieved_messages
    # total_messages = [message.message for message in total_messages_objects]
    return jsonify(recieved=recieved_messages, sent=sent_messages)