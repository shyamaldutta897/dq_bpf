from pyspark.sql.functions import *

def check_fare_amount(df,column):
    total_rows=df.count()
    valid_rows=df.filter(col(column).isNotNull())
    failed=valid_rows.filter((col(column).cast('double')<0)).count()

    return{
          'field':column,
          'check':'Negative value',
          'total_rows':total_rows,
          'failed_rows':failed,
          'percentage':(failed/total_rows)  
          } 


