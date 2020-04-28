''' Task 2 '''
import json
import http.client
import asciitable
from task_1 import Task


class SecondTask:
    ''' Second Task Class'''
    @staticmethod
    def api_builder(api_tag):
        '''
        To build the API with the given interface name
        or for all the interfaces.
        '''
        return '/interface/' + str(api_tag)

    @staticmethod
    def api_get_function(api):
        '''
        To fire the GET request and get the response.
        '''
        connection = http.client.HTTPConnection('127.0.0.1', 5000, timeout=10)
        connection.request('GET', api)
        response = connection.getresponse()
        return response

    @staticmethod
    def ascii_table_creator(response_list):
        '''
        To create the ASCII TABLE with the given
        response data.
        '''
        for response in response_list:
            response_data = str(response).lstrip('b\'').rstrip('\\n\'')
            response_data = json.loads(response_data)
            headers = response_data[0].keys()
            values = [list(j.values()) for i, j in enumerate(response_data)]
            asciitable.write(values, names=headers,
                             Writer=asciitable.FixedWidthTwoLine, delimiter='|')


if __name__ == "__main__":
    def main(api_parameter):
        ''' Main Function '''
        try:
            api = SecondTask.api_builder(api_parameter)
            response_list = SecondTask.api_get_function(api)
            SecondTask.ascii_table_creator(response_list)
        except:
            print('Encountered a problem. Please check!!')

    OBJ = Task.load_config_file('config.txt')
    DATA = [json.loads(data) for data in Task.data_parser(OBJ)]
    INTERFACE_LIST = [i['interface'] for i in DATA]
    INTERFACE_LIST.append('all')
    for param in INTERFACE_LIST:
        main(param)
        print('\n')
