import hashlib
import random
import string


# These functions just make password, salt it and allow for 
# me to actually check that salt and hashed pw in the users
# table in the db. 

#please replace INSERT_RANDOM_INT_HERE with a random int value to setup salting
def make_salt1():
    return ''.join([random.choice(string.ascii_letters)for x in range(5)])

def make_pw_hash(password, salt=None):
    if not salt:
        try:
            from secrets import make_salt
            salt = make_salt()
        except ImportError:
            salt = make_salt1()
    hash = hashlib.sha256(str.encode(password + salt)).hexdigest()
    return '{0},{1}'.format(hash,salt)


def check_pw_hash(password, hash):
    salt = hash.split(',')[1]
    if make_pw_hash(password, salt) == hash:
        return True
    else:
        return False


