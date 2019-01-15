# coding = utf-8
"""
@author: zhou
@time:2019/1/15 11:17
"""


from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class AdminUser(db.Model):
    __tablename__ = 'adminuser'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @staticmethod
    def init_user():
        users = AdminUser.query.filter_by(username='admin').first()
        if users is None:
            users = AdminUser(username='admin')
        users.password = 'hardtoguess'
        db.session.add(users)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Users {}>".format(self.username)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, index=True)
    picture_count = db.Column(db.Integer)


class Picture(db.Model):
    __tablename__ = 'pictures'
    id = db.Column(db.Integer, primary_key=True)
    picture_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    picture_name = db.Column(db.String(128))
    picture = db.Column(db.Text)



