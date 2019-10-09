from sql_alchemy_db_instance import db
from hashutils import make_pw_hash, make_salt, check_pw_hash

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500))
    pw_hash = db.Column(db.String(500))

    def __init__(self, username, password):
        self.username = username
        self.pw_hash = make_pw_hash(password)