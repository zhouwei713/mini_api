# coding = utf-8
"""
@author: zhou
@time:2019/1/15 15:46
"""


from . import api_1_0
from flask import jsonify

''''
@api_1_0.app_errorhandler(404)
def not_found(e):
    print(e)
    error_info = '{}'.format(e)
    response = jsonify({'error': error_info})
    response.status_code = 404
    return response


@api_1_0.app_errorhandler(403)
def forbidden(e):
    print(e)
    error_info = '{}'.format(e)
    response = jsonify({'error': error_info})
    response.status_code = 403
    return response
'''