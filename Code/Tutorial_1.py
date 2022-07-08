
import pymysql
pymysql.install_as_MySQLdb()

import pandas as pd

import warnings
warnings.filterwarnings("ignore")

# Your Database connection
mydb = pymysql.connect(
    host='localhost', 
    user='tahir', 
    password=''
)
mycursor = mydb.cursor()


############ SELECT ALL TABLE ############ If you want to select all columns use this query and comment other queries
query = '''
    SELECT 
        *
    FROM
        classicmodels.employees;
'''

############ SELECT ONE OR MORE COLUMNS ############ If you want to select specific column or columns use this query and comment other queries
query = '''
    SELECT 
        employeeNumber, firstName, lastName
    FROM
        classicmodels.employees;
'''

# Execute the query
mycursor.execute(query)
result = mycursor.fetchall()

# Get the column names from table
headers = [i[0] for i in mycursor.description]

# Convert your query result ----> Dataframe.
df = pd.DataFrame(result, columns=headers)

# Print result
print(f'\n\n{df}\n\n')
