import json
import functions
from cpu import cpu
from storage import storage
from network import network
from memory import memory
from functions import url



class Executor:
    def __init__(self, json_file_name="commands.json"):
        with open(json_file_name, 'r') as fp:
            self._json = json.load(fp)
        self.network = self._json["network"]
        self.cpu = self._json["cpu"]
        self.memory = self._json["memory"]
        self.storage = self._json["storage"]
        self.system = self._json['system']
        self.curr_time = functions.curr_time()
        self.system_data = functions.system(self.system)
        self.send_data(self.system_data, 'system')

        fp.close()

    def exec_command(self):
        # import pdb
        # pdb.set_trace()
        if functions.curr_time() - self.curr_time >= 1:
            data = {
                'network': network(self.network),
                'cpu':cpu(self.cpu),
                'storage': storage(self.storage),
                'memory': memory(self.memory),
                'timestamp': functions.curr_time(),
                'id': self.system_data['id']
            }

        # pdb.set_trace()
            print data['timestamp']
            self.send_data(data, 'live')
            self.curr_time = functions.curr_time()

    def send_data(self, data, param):
        functions.post_request(data, self.generate_url(param))

    def generate_url(self, param):
        return str(url['protocol'] + url['ip'] + ':' + url['port'] + url[param])
