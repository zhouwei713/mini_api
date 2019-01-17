# coding = utf-8
"""
@author: zhou
@time:2019/1/15 12:55
"""

from app import db
from flask_restful import Api, Resource
from flask import request, url_for
from app.api_1_0 import api_1_0
from ..models import User, Picture, AdminUser
from app.api_1_0.api_auth import auth
from flask import jsonify
import os
import time
from werkzeug.utils import secure_filename
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


api_user = Api(api_1_0)


class UserAddApi(Resource):
    @auth.login_required
    def post(self):
        print("开始调用useradd接口")
        user_info = request.get_json()
        try:
            u = User(username=user_info['username'])
            p = Picture(picture_name=user_info['username'])
            u.picture_count = user_info['picture_count']
            db.session.add(u)
            db.session.add(p)
            db.session.commit()
        except:
            logger.info("User add: {} failure...".format(user_info['username']))
            db.session.rollback()
            return False
        else:
            logger.info("User add: {} success...".format(user_info['username']))
            return True
        finally:
            db.session.close()


class TestAPI(Resource):
    def post(self):
        print("调用test")
        if 'PID' not in request.files:
            return jsonify({'code': -1, 'filename': '', 'msg': 'please select one picture to upload'})
        user = request.form.get('UID')
        f = request.files['PID']
        basepwd = os.getcwd()
        pwd = os.path.join(basepwd, r'app')
        tmp_path = os.path.join(pwd, r'static/%s' % user)
        new_filename = str(time.time()) + '.' + f.filename.split('.')[1]
        if not os.path.exists(tmp_path):
            os.makedirs(tmp_path)
            upload_path = os.path.join(tmp_path, secure_filename(new_filename))
            f.save(upload_path)
            if User.query.filter_by(username=user).first():
                u = User.query.filter_by(username=user).first()
                u.picture_count += 1
                p = Picture(picture_name=user, picture=upload_path, picture_id=u.id)
                db.session.add(u)
                db.session.add(p)
                db.session.commit()
            else:
                newu = User(username=user)
                db.session.add(newu)
                db.session.commit()
                newp = Picture(picture_name=user, picture=upload_path, picture_id=newu.id)
                db.session.add(newp)
                db.session.commit()
        else:
            upload_path = os.path.join(tmp_path, secure_filename(new_filename))
            f.save(upload_path)
            if User.query.filter_by(username=user).first():
                u = User.query.filter_by(username=user).first()
                u.picture_count += 1
                p = Picture(picture_name=user, picture=upload_path, picture_id=u.id)
                db.session.add(u)
                db.session.add(p)
                db.session.commit()
            else:
                newu = User(username=user)
                db.session.add(newu)
                db.session.commit()
                newp = Picture(picture_name=user, picture=upload_path, picture_id=newu.id)
                db.session.add(newp)
                db.session.commit()
        db.session.close()
        return jsonify({"p_url": 'http://127.0.0.1:9980/static/%s/' % user + new_filename})


class AdminUserVerifyApi(Resource):
    @auth.login_required
    def post(self):
        user_info = request.get_json()
        try:
            u = AdminUser.query.filter_by(username=user_info['username']).first()
            if u is None or u.verify_password(user_info['password']) is False:
                logger.info("User query: {} failure...".format(user_info['username']))
                return False
        except:
            logger.info("User query: {} failure...".format(user_info['username']))
            return False
        else:
            logger.info("User query: {} success...".format(user_info['username']))
            return True
        finally:
            db.session.close()


api_user.add_resource(UserAddApi, '/useradd', endpoint='useradd')
api_user.add_resource(AdminUserVerifyApi, '/userverify', endpoint='userverify')
api_user.add_resource(TestAPI, '/test', endpoint='test')



