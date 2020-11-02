'''
To read csv file and to connect to database
'''

import csv
import pymongo

class Csv:
    @staticmethod
    def read_csv(file_path):
        '''
        To read csv file
        :param file_path: file location path
        :return: generator object
        '''
        with open(file_path, 'r') as a:
            cs_r = csv.DictReader(a)
            yield cs_r
class MongoDb:
    @staticmethod
    def db_details(host,port_number,db_name,collection_name):
        '''
        method to connect datbase
        :param host:db host
        :param port_number:db port_number
        :param db_name:database name
        :param collection_name:collection name
        :return:db driver
        '''
        mongo_client = pymongo.MongoClient(host, port_number)
        mongo_db = mongo_client[db_name]
        collection_name = collection_name
        db_connect = mongo_db[collection_name]
        return db_connect




