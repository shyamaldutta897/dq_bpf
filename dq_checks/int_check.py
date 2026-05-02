from pyspark.sql.functions import *

def int_check(df,column):
    total=df.count()
    failed=df.filter(typeof(column)!="int").count()

    return
    {   "field":column,
        "total_rows":total,
        "failed_rows":failed,
        "percentage":failed/total
    } 

    