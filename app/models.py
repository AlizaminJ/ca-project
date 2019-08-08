from app import db
# models.py
# 
# Used to model our datastore
# The post model is used to handle the posts any one can make
# This model allows us to only care about how the object looks, 
# and not care about how it is serialized

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_name = db.Column(db.String(40))
    title = db.Column(db.String(50))

    def __repr__(self):
        return '<Post %r>' % (self.body)
