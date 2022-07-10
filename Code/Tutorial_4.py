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

############ DISTINCT ############ 
query = '''
    SELECT DISTINCT
        lastname
    FROM
        employees
    ORDER BY lastname;
'''

############ DISTINCT AND NULL VALUES ############ 
query = '''
    SELECT DISTINCT
        state
    FROM
        customers;
'''

############ DISTINCT WITH MULTIPLE COLUMNS ############ 
query = '''
    SELECT DISTINCT
        state, city
    FROM
        customers
    WHERE
        state IS NOT NULL
    ORDER BY state , city;
'''

# Execute the query
mycursor.execute(query)
result = mycursor.fetchall()

# Get the column names from table
headers = [i[0] for i in mycursor.description]

# Convert your query result ----> Dataframe.
df = pd.DataFrame(result, columns=headers)

print()
print(df)
print()