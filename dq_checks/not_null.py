from pyspark.sql.functions import *

def check_not_null(df,col):
    total_rows=df.count()
    failed=df.filter(col(col).isNull()).count()

    return{
          'field':col,
          'total_rows':total_rows,
          'failed_rows':failed,
          'percentage':(failed/total_rows)  
          } 


