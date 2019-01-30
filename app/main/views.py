# coding = utf-8
"""
@author: zhou
@time:2019/1/15 12:36
"""

from .. import db
from . import main
from ..models import User
from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename


@main.route('/editcase')
def editcase():

    return render_template('test02.html')


@main.route('/testxlsx')
def testxlsx():
    return render_template('test03.html')



