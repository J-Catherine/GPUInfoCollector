from flask_script import Manager
from flask import Flask, render_template, jsonify
import os
import pymongo
import json
import datetime
import time

basedir = os.path.abspath(os.path.dirname(__file__))
TIME = [0]

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = '1qa2dzc12edcd1f8zschew211'


# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp


app.after_request(after_request)

manager = Manager(app)


def read_info():
    mongo_client = pymongo.MongoClient(host="localhost", port=27017)
    gpu_db = mongo_client.gpustat
    d = dict()
    for ip in gpu_db.list_collection_names():
        if ip.startswith('10.141'):
            collection = gpu_db[ip]
            results = collection.find().sort('time', pymongo.DESCENDING)
            result = dict()
            for r in results:
                if r['index'] not in result:
                    del r['_id']
                    r['time'] = (r['time'] + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
                    result[r['index']] = r
                else:
                    break
            d[ip] = [result[r] for r in sorted(result.keys())]
    with open("../data/record.json", 'w') as f:
        json.dump(d, f)


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/data/all', methods=['GET'])
def get_data():
    if time.time() - TIME[0] >= 30:
        TIME[0] = time.time()
        print("change:", TIME[0])
        read_info()
    with open("../data/record.json", 'r') as f:
        return jsonify(json.load(f))


# @app.route('/detail/<uuid>', methods=['GET'])
# def detail(uuid):
#     pass


@app.errorhandler(404)
def page_not_found(_):
    return render_template('404.html'), 404


@manager.command
def run():
    app.run(port=8997, host='10.141.221.112', debug=False)


@manager.command
def dev():
    app.run(port=18997, host='10.141.221.112', debug=True)


if __name__ == '__main__':
    manager.run()
