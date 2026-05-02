from pyspark.sql.functions import *

def double_check(df,column):
    total=df.count()
    failed=df.filter(typeof(column)!="double").count()

    return
    {   "field":column,
        "total_rows":total,
        "failed_rows":failed,
        "percentage":failed/total
    } 

    