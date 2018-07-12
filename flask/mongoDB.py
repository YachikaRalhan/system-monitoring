from pymongo import MongoClient
from bson import json_util
import json
import os
import pymongo

class Mongo:

    def __init__(self, database, system):
	self.client = MongoClient(os.environ['DB'],27017, serverSelectionTimeoutMS=20, connectTimeoutMS=1000)
        # try:
        #     info = self.client.server_info()
        # except Exception as e:
        #     print("server is down.")
        self.database = self.client[database]
        self.coll = self.database[system]

    def insert(self, data):
        import pdb
        # pdb.set_trace()
        data['hostname'] = self.coll.insert_one(data)

    def read(self):
        list = self.coll.distinct("hostname")
        hostList = []
        for l in list:
            hostList.append(l)

        return json.loads(json_util.dumps(hostList))
        

    def systemObject(self, hostname):
        if hostname:
            info = self.coll.find_one({"hostname": hostname})

            return json.loads(json_util.dumps(info))

    def check(self):
        try:
            if self.database.collection_names() == []:
                return "connected"
        except:
            return "mongo container is not running"


