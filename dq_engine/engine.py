
from dq_checks.not_null import check_not_null
from dq_checks.negative_amount import check_fare_amount
from dq_checks.int_check import int_check
from dq_checks.double_check import double_check
from configs.config_loader import load_config

def run_checks(df,config_path):

    rules=load_config(config_path)

    check_map={
        "not_null":check_not_null,
        "negative_amount":check_fare_amount,
        "num_check":int_check,
        "double_check":double_check
    }


    for rule in rules:
        func=check_map[rule["type"]]
        for column in rule["columns"]:
            func(df,column)
   


