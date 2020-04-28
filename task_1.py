''' Task 1 '''
from ciscoconfparse import CiscoConfParse
from flask import Flask, json, abort, jsonify

class Task:
    '''First Task Class'''

    @staticmethod
    def load_config_file(config_file):
        '''
        Method to load the config file.
        '''
        return CiscoConfParse(config_file)

    @staticmethod
    def data_parser(raw_data):
        '''
        To parse the data read from the config file.
        '''
        interfaces = raw_data.find_objects(r"^interface ")
        json_data_list = []
        for interface in interfaces:
            json_data = {}
            json_data['interface'] = interface.re_match_typed(
                r'^interface\s+(\S.+?)$')
            json_data['ip_address'] = interface.re_match_iter_typed(
                r'ip\saddress\s(\d+\.\d+\.\d+\.\d+)\s', result_type=str,
                group=1, default='No IP Address Found')
            json_data['subnet'] = interface.re_match_iter_typed(
                r'ip\saddress\s(\d+\.\d+\.\d+\.\d+)\s(\d+\.\d+\.\d+\.\d+)', result_type=str,
                group=2, default='No Subnet Found')
            json_data['description'] = interface.re_match_iter_typed(
                r'description\s(.*)', result_type=str, group=1, default='No Description Found')
            json_data_list.append(json.dumps(json_data))
        return json_data_list

if __name__ == "__main__":
    OBJ = Task.load_config_file('config.txt')
    DATA_LIST = Task.data_parser(OBJ)
    DATA = [json.loads(data) for data in DATA_LIST]
    API = Flask(__name__)

    @API.route('/interface/all', methods=['GET'])
    def get_all_data():
        ''' To request all the data'''
        return jsonify(DATA)

    @API.route('/interface/<path:interface_name>', methods=['GET'])
    def get_interface_data(interface_name):
        ''' To request only for a selected interface '''
        interface_data = [i for i in DATA if str(
            i['interface']) == str(interface_name)]
        if not interface_data:
            abort(404)
        return jsonify(interface_data)

    API.run()
