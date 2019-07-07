from flask_script import Manager
from flask import Flask, render_template, jsonify
import os
import pymongo
import json
import time

basedir = os.path.abspath(os.path.dirname(__file__))
TIME = [0]

app = Flask(__name__)
app.config['SECRET_KEY'] = '1qa2dzc12edcd1f8zschew211'

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
                    del r['time']
                    result[r['index']] = r
                else:
                    break
            d[ip] = [result[r] for r in sorted(result.keys())]
    with open("../data/record.json", 'w') as f:
        json.dump(d, f)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/data/all', methods=['GET'])
def get_data():
    if time.time() - TIME[0] >= 30:
        TIME[0] = time.time()
        print("change:", TIME[0])
        read_info()
    with open("../data/record.json", 'r') as f:
        return jsonify(json.load(f))


@app.errorhandler(404)
def page_not_found(_):
    return render_template('404.html'), 404


@manager.command
def run():
    app.run(port=18999, host='10.141.221.112', debug=False)


if __name__ == '__main__':
    manager.run()
