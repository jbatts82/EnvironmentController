###############################################################################
# File Name  : models.py
# Date       : 08/25/2020
# Description: P
###############################################################################

from datetime import datetime
from WebApp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)    
 
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
class Sensor_Reading(db.Model):
    time_stamp = db.Column(db.DateTime, primary_key=True, index=True, default=datetime.utcnow)
    temp_f = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    humidity = 
    

    
    
    
    
    