from sql_alchemy_db_instance import db
from hashutils import make_pw_hash, make_salt, check_pw_hash

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500))
    pw_hash = db.Column(db.String(500))
    images = db.relationship('Images', backref='users', lazy=True)
    likedimages = db.relationship('LikedImages', backref='users', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.pw_hash = make_pw_hash(password)


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    likedimages = db.relationship('LikedImages', backref='images', lazy=True)


class LikedImages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_link = db.Column(db.String, db.ForeignKey('images.link'),
        nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    isliked = db.Column(db.Boolean, default=True, nullable=False)