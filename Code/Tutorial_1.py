import pymysql
pymysql.install_as_MySQLdb()

import pandas as pd

import warnings
warnings.filterwarnings("ignore")

# Your Database connection
mydb = pymysql.connect(
    host='localhost', 
    user='tahir', 
    password='',
    database='classicmodels'
)
mycursor = mydb.cursor()


############ SELECT ALL TABLE ############ 
query = '''
    SELECT 
        *
    FROM
        employees;
'''

############ SELECT ONE OR MORE COLUMNS ############ 
query = '''
    SELECT 
        employeeNumber, firstName, lastName
    FROM
        employees;
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
