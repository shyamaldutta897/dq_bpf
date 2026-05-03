from pyspark.sql.functions import *

def double_check(df,column):
    total=df.count()
    failed=df.filter(typeof(column).cast(str)!="double").count()

    return
    {   "field":column,
        "check":"Datatype - double",
        "total_rows":total,
        "failed_rows":failed,
        "percentage":failed/total
    }  

    