'''
This module is for processing data from csv files and database
'''

import utils
import json

class Data_Process:
    '''
    class contains methods for data operations
    '''
    def __init__(self,host,port,db,col,path):
        self.host = host
        self.port = port
        self.db = db
        self.col = col
        self.path = path

    def count_Records(self):
        '''
        Method to count the records in collection and return the record count
       '''
        record_count = utils.MongoDb.db_details(self.host,self.port,self.db,self.col).find().count()
        return record_count

    def sort_record_ascending_order(self):
        '''
        Method to sort record in ascending order and return sorted records in cursor obj
        '''
        sorted_records = utils.MongoDb.db_details(self.host,self.port,self.db,self.col).find().sort("Total Profit", 1)
        return sorted_records

    def insert_each_record(self):
        '''
        Method to insert each record from generator object to mongodb
        '''
        for records in utils.Csv.read_csv(self.path):
            for each_record in records:
                utils.MongoDb.db_details(self.host, self.port, self.db, self.col).insert(each_record)











