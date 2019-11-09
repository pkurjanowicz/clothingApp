from sql_alchemy_db_instance import db
from hashutils import make_pw_hash, check_pw_hash
from sqlalchemy import UniqueConstraint

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500))
    pw_hash = db.Column(db.String(500))
    time_zone = db.Column(db.String(120))
    images = db.relationship('Images', backref='users', lazy=True)
    likedimages = db.relationship('LikedImages', backref='users', lazy=True) 
    #flask sqlalchemy magic(line above this).
    # This actually allows us to reference the User's table in 
    # other tables like images and likedimages using the backref function
    # this documentation explains it: https://docs.sqlalchemy.org/en/13/orm/backref.html

    def __init__(self, username, password):
        self.username = username
        self.pw_hash = make_pw_hash(password) #checking salted and hashed pass


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(120), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    likedimages = db.relationship('LikedImages', backref='images', lazy=True)


class LikedImages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_link = db.Column(db.String, db.ForeignKey('images.link'),
        nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(600),nullable=False)
    first_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    second_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message_time_utc = db.Column(db.String(200),nullable=False)