from models import Users
from datetime import datetime
from dateutil import tz

#This function is used in the messagesAPI.py file to just simply convert the user
#messages to whatever timezone they have set. It will default to GMT if the user hasn't set it up yet
#GMT is how we store it in the database

def calculate_current_time_zone(message_time,user_id):
    user_timezone = Users.query.filter_by(id=user_id).first().time_zone
    if user_timezone == 'PacificTime':
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('America/Los_Angeles')
        utc = datetime.strptime(message_time, '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=from_zone)
        new_time = utc.astimezone(to_zone)
        return new_time
    if user_timezone == 'EasternTime':
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('America/New_York')
        utc = datetime.strptime(message_time, '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=from_zone)
        new_time = utc.astimezone(to_zone)
        return new_time
    if user_timezone == "MountainTime":
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('America/Denver')
        utc = datetime.strptime(message_time, '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=from_zone)
        new_time = utc.astimezone(to_zone)
        return new_time
    if user_timezone == "CentralTime":
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('America/Chicago')
        utc = datetime.strptime(message_time, '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=from_zone)
        new_time = utc.astimezone(to_zone)
        return new_time
    else:
        return message_time+' GMTxxxxxx'

    


