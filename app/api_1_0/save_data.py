# coding = utf-8
"""
@author: zhou
@time:2019/1/29 17:00
"""


from app import db
from flask_restful import Api, Resource
from flask import request, url_for
from app.api_1_0 import api_1_0
from ..models import TestCase
from app.api_1_0.api_auth import auth
from flask import jsonify
import os
import time
from werkzeug.utils import secure_filename
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


save_data = Api(api_1_0)


class AutoSaveData(Resource):
    def post(self):
        data = str(request.data, encoding='utf-8')
        global null
        null = ''
        data_dict = eval(data)
        # print(data)
        # print(type(data))
        # print(data_dict['data'])
        return jsonify({"result": "ok"})


class SaveData(Resource):
    def post(self):
        data = str(request.data, encoding='utf-8')
        global null
        null = ''
        data_dict = eval(data)
        d = data_dict['data']
        for i in d:
            check = TestCase.query.filter_by(id=i[0]).first()
            if check:
                check.casename = i[1]
                check.casestep = i[2]
                db.session.commit()
            else:
                t = TestCase(id=i[0], casename=i[1], casestep=i[2])
                db.session.add(t)
                db.session.commit()
        db.session.close()
        return jsonify({"result": "ok"})


class SaveToTest(Resource):
    def post(self):
        data = str(request.data, encoding='utf-8')
        global null
        null = ''
        data_dict = eval(data)
        d = data_dict['data']
        for i in d:
            check = TestCase.query.filter_by(id=i[0]).first()
            if check:
                check.name = i[1]
                check.project = i[2]
                db.session.commit()
            else:
                t = TestCase(id=i[0], casename=i[1], casestep=i[2])
                db.session.add(t)
                db.session.commit()
        db.session.close()
        return jsonify({"result": "ok"})


class SaveToNew(Resource):
    def post(self):
        data = str(request.data, encoding='utf-8')
        global null
        null = ''
        data_dict = eval(data)
        d = data_dict['data']
        for i in d:
            check = TestCase.query.filter_by(id=i[0]).first()
            if check:
                check.account = i[1]
                check.username = i[2]
                check.hobby = i[3]
                check.ability = i[4]
                check.freq = i[5]
                check.fv = i[6]
                db.session.commit()
            else:
                t = TestCase(id=i[0], account=i[1], username=i[2],
                             hobby=i[3], ability=i[4], freq=i[5],
                             fv=i[6])
                db.session.add(t)
                db.session.commit()
        db.session.close()
        return jsonify({"result": "ok"})


save_data.add_resource(SaveData, '/savedata', endpoint='savedata')
save_data.add_resource(AutoSaveData, '/autosavedata', endpoint='autosavedata')
save_data.add_resource(SaveToTest, '/savetotest', endpoint='savetotest')
save_data.add_resource(SaveToNew, '/savetonew', endpoint='savetonew')

