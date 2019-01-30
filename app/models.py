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
    picture_count = db.Column(db.Integer, default=1)


class Picture(db.Model):
    __tablename__ = 'pictures'
    id = db.Column(db.Integer, primary_key=True)
    picture_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    picture_name = db.Column(db.String(128))
    picture = db.Column(db.Text)


class TestCase(db.Model):
    __tablename__ = 'testcase'
    id = db.Column(db.String(128), primary_key=True)
    casename = db.Column(db.String(128))
    casestep = db.Column(db.Text)
    caseproject = db.Column(db.String(128))


class Testtable(db.Model):
    __tablename__ = 'testtable'
    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128))
    project = db.Column(db.String(128))


class TestNew(db.Model):
    __tablename__ = 'testnew'
    id = db.Column(db.String(128), primary_key=True)
    account = db.Column(db.String(128))
    username = db.Column(db.String(128))
    hobby = db.Column(db.String(128))
    ability = db.Column(db.String(128))
    freq = db.Column(db.String(128))
    fv = db.Column(db.String(128))



