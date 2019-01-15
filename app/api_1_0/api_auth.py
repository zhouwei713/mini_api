# coding = utf-8
"""
@author: zhou
@time:2019/1/15 12:53
"""

from flask_httpauth import HTTPBasicAuth
from flask import jsonify
from ..models import AdminUser


auth = HTTPBasicAuth()


@auth.error_handler
def unauthorized():
    error_info = '{}'.format("Invalid credentials")
    print(error_info)
    response = jsonify({'error': error_info})
    response.status_code = 403
    return response


@auth.verify_password
def verify_password(username, password):
    user = AdminUser.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    return True

