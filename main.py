import run
import json

with open('config.json') as config_file:
        data = json.load(config_file)
        
if __name__ == '__main__':
    
    Sales_Record = run.Data_Process(data['host'],data['port_number'],data['db_name'],data['coll_name'],data['path'])
    Sales_Record.count_Records() #method call to retrieve record count

    Store_sorted_records = Sales_Record.sort_record_ascending_order() # call this method retrieve sorted records
    Sales_Record.insert_each_record()   # call this method to store each record into database


