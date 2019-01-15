# coding = utf-8
"""
@author: zhou
@time:2019/1/15 12:55
"""

from app import db
from flask_restful import Api, Resource
from flask import request
from app.api_1_0 import api_1_0
from ..models import User, Picture, AdminUser
from app.api_1_0.api_auth import auth
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


api_user = Api(api_1_0)


class UserAddApi(Resource):
    @auth.login_required
    def post(self):
        user_info = request.get_json()
        try:
            u = User(username=user_info['username'])
            p = Picture(picture_name=user_info['username'])
            u.password = user_info['password']
            u.picture_count = user_info['picture_count']
            db.session.add(u)
            db.session.add(p)
            db.session.commit()
        except InterruptedError:
            logger.info("User add: {} failure...".format(user_info['username']))
            db.session.rollback()
            return False
        else:
            logger.info("User add: {} success...".format(user_info['username']))
            return True
        finally:
            db.session.close()


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



