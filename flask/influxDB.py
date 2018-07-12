from influxdb import InfluxDBClient
import json
import os

class Influx:
    def __init__(self, host="os.environ['influx']", port=8086, user='root', password='root', dbname='influx-db'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname

        self.client = InfluxDBClient(self.host, self.port, self.user, self.password, self.dbname)

        self.client.create_database(self.dbname)

    def write_data(self, influxData):
        influxData['data'] = json.dumps(influxData['data'])
        influxData['cpu'] = json.dumps(influxData['cpu'])
        influxData['storage'] = json.dumps(influxData['storage'])
        influxData['memory'] = json.dumps(influxData['memory'])

        json_body = [
            {
                "measurement": "network",

                "tags": {
                    "host": influxData['id'],
                },
                "time": influxData['timestamp']*1000000000,

                "fields": {
                    "data": influxData['data'],
                    "cpu": influxData['cpu'],
                    "memory" :influxData['memory'],
                    "storage" :influxData['storage']

                }
            }
        ]

        self.client.write_points(json_body)


    def liveObject(self, hostname, fromEpoch, toEpoch):
        query = "select * from network where time >= {} and time < {} and host = '{}'".format(fromEpoch, toEpoch, hostname)
        data = self.client.query(query)
        return json.dumps(data.raw)

    def check(self):
        try:
            if self.client.get_list_database():
                return "connected" 
        except:
            return "not connected"
    


