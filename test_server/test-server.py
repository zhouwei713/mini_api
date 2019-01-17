# coding = utf-8
"""
@author: zhou
@time:2019/1/16 14:40
"""


from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def Forst():
    return "hello Guys"


url = 'http://127.0.0.1:9980/api/useradd'


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'code': -1, 'filename': '', 'msg': 'please select one picture to upload'})
        f = request.files['file']
        user_input = request.form.get("name")
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, r'static/', secure_filename(f.filename))
        f.save(upload_path)
        return render_template('upload_ok.html', userinput=user_input, filename=f.filename)
    return render_template('upload.html')


@app.route('/jsupload', methods=['POST', 'GET'])
def jsupload():
    return render_template('js_upload.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='9981', debug=True)
