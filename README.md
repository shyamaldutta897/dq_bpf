                              ******** DATA QUALITY FRAMEWORK FOR NYC TAXI DATASET ********

The framework is having 5 modules - 

1. utils - All utility related codes. As of now SparkSession is defined here.

2. configs - 
    a. All configuration related files. It holds a json file called user_rules.json which holds all the checks to be applied over the dataset. The file holds the below parameters - 
        i. columns - A list of fields on which a specific check should be applied
        ii. type - The check name, in reality this is a UDF name which would be later called dynamically.
        iii. check - The description for the check
        iv. threshold - The miimum percentage of good quality data expected from the fields mentioned ins columns key.
    b. The configs folder also holds a script called config_loader.py which helps to read the user_rules.json file.

3. dq_checks - 
    a. This module contains all UDFs that would be responsible for different checks across different fields.
        i. Each and every UDF accepts a DF and a field.
        ii. Runs predefined logics on top of the called field from the DF
        iii. Return a dict that looks like below - 
             return{
                    "field":the name_of the field, comes from the column parameter of the UDF
                    "check":The check description, a manual field.
                    "total_rows":Total item count of the called field.
                    "failed_rows":Failed item count of the called field based on predefined check.
                    "percentage":Percentage - failed/total
                     }  
    b. Current UDF list - 
        i. check_not_null - To check how many line items of a given list having not null values.
        ii. check_fare_amount - To check what if any fare amount is having negative value.
        iii. int_check - To check if certain fields are having datatype int or not.
        iv. double_check - To check if any field is having datatype double or not.

4. dq_engine - This folder is the head of this entire dataframe. It contains a script called engine.py.
    a. All functions from all .py files are called here.
    b. A new UDF called run_checks is defined with two parameters - df, config_path
    c. DF is for the dataframe we want to process and config_path is for the file where rules are sitting.

5. pipelines - The final module where actual execution happens.
    a. The execution happens in a colab notebook.
    b. Reason behind colab - Need to execute some of the Spark code in the framework. Colab is straightforward
    c. Load the data from a file sitting in drive as a DF.
    d. Run the run_checks function on top of this DF
    e. Write the output to a new file, target is drive.
 

Entry point - dq_pipelines.ipynb

Flow - 

configs --> dq_checks --> dq_engine --> utils --> pipelines



        
