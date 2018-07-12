# !/usr/bin/env python

from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from mongoDB import Mongo
from influxDB import Influx
import json
import os

app = Flask(__name__)
api = Api(app)

cors = CORS(app)

class System(Resource):
    def post(self):
        data = request.data
        jsondata = json.loads(data)
        formedData = {}
        formedData['hostname'] = jsondata['id']
        formedData['data'] = json.dumps(jsondata)
        mongo = Mongo('database', 'system')
        mongo.insert(formedData)


class Live(Resource):
    def post(self):
        data = request.data
        jsondata = json.loads(data)
        influxData = {}
        influxData['id'] = jsondata['id']
        influxData['timestamp'] = jsondata['timestamp']
        influxData['data'] = jsondata['network']
        influxData['cpu'] = jsondata['cpu']
        influxData['storage'] = jsondata['storage']
        influxData['memory'] = jsondata['memory']
        influx = Influx(host=os.environ['influx'], port=8086, user='root', password='root', dbname='influx-db')
        influx.write_data(influxData)


class Hosts(Resource):
    def get(self):
        mongo = Mongo('database', 'system')
        return mongo.read()


class systemHost(Resource):
    def get(self, hostname):
        mongo = Mongo('database', 'system')
        return mongo.systemObject(hostname)


class liveHost(Resource):
    def get(self, hostname,fromEpoch,toEpoch):
        influx = Influx(host="os.environ['influx']", port=8086, user='root', password='root', dbname='influx-db')
        return influx.liveObject(hostname,fromEpoch,toEpoch)

class health(Resource):
    def get(self):
        health = {}
        mongo = Mongo('database', 'system')
        health["mongo"] = mongo.check()
        try:
            influx = Influx(host=os.environ['influx'], port=8086, user='root', password='root', dbname='influx-db')
            health["influx"] = influx.check()
        except:
            health["influx"] = "influx container is not running"
        return health


api.add_resource(System, '/system')
api.add_resource(Live, '/live')
api.add_resource(Hosts, '/hostnames')
api.add_resource(systemHost, '/data/system/<string:hostname>')
api.add_resource(liveHost, '/data/live/<string:hostname>/<fromEpoch>/<toEpoch>')
api.add_resource(health,'/health')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8089, debug=True)
    app.run(use_reloader=True)