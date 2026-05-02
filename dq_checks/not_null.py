from pyspark.sql.functions import *

def check_not_null(df,column):
    total_rows=df.count()
    failed=df.filter(col(column).isNull()).count()

    return{
          'field':column,
          'total_rows':total_rows,
          'failed_rows':failed,
          'percentage':(failed/total_rows)  
          }  


