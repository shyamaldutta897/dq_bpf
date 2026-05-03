from pyspark.sql.functions import *

def int_check(df,column):
    total=df.count()
    failed=df.filter(typeof(column).cast(string)!="double").count()

    return
    {   "field":column,
        "check":"Datatype - int",
        "total_rows":total,
        "failed_rows":failed,
        "percentage":failed/total
    } 

    