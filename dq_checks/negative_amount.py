from pyspark.sql.functions import *

def check_fare_amount(df,column):
    total_rows=df.count()
    failed=df.filter(column<0).count()

    return{
          'field':column,
          'total_rows':total_rows,
          'failed_rows':failed,
          'percentage':(failed/total_rows)  
          } 


