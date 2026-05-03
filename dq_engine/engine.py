
import sys
sys.path.append("D:/DQ_framework") #This is needed to test this file locally.

from dq_checks.not_null import check_not_null
from dq_checks.negative_amount import check_fare_amount
from dq_checks.int_check import int_check
from dq_checks.double_check import double_check
from configs.config_loader import load_config

def run_checks(df,config_path):

    rules=load_config(config_path) #loading the file from config path

    #hash map, to use with the final execution
    check_map={ 
        "not_null":check_not_null,
        "negative_amount":check_fare_amount,
        "num_check":int_check,
        "double_check":double_check
    }

    result=[]

    #looping over the file
    for rule in rules['rules']:
        func=check_map[rule["type"]] #maping the function name from the hash map defined above
        for column in rule["columns"]: #Looping over the columns field
            op=func(df,column) #storing the output of each column from teh function in op var
            result.append(op) #appening to the result list
    return result





     
    












   


