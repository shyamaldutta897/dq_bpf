from pyspark.sql.functions import *

def check_fare_amount(df,col):
    total_rows=df.count()
    failed=df.filter(col<0).count()

    return{
          'field':col,
          'total_rows':total_rows,
          'failed_rows':failed,
          'percentage':(failed/total_rows)  
          }


