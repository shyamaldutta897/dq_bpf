from pyspark.sql.functions import *
from pyspark.sql.types import *

def int_check(df,column):
    total=df.count()
    failed=df.filter(typeof(column).cast(StringType())!="double").count()

    return
    {   "field":column,
        "check":"Datatype - int",
        "total_rows":total,
        "failed_rows":failed,
        "percentage":failed/total
    }  

    