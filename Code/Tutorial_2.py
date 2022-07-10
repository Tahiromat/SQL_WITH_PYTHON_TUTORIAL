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

############ ORDER BY DESC ############ 
query = '''
    SELECT 
        contactFirstname, contactLastname
    FROM
        customers
    ORDER BY contactLastname DESC;
'''

############ ORDER BY ASC ############ 
query = '''
    SELECT 
        contactFirstname, contactLastname
    FROM
        customers
    ORDER BY contactLastname ASC;
'''

############ ORDER BY ASC AND DESC ############ 
query = '''
    SELECT 
        contactLastname, contactFirstname
    FROM
        customers
    ORDER BY contactLastname DESC , contactFirstname ASC;
'''


############ BASIC OPERATIONS WITH COLUMNS AND ORDER BY ############ 
query = '''
    SELECT 
        quantityOrdered, priceEach, quantityOrdered * priceEach
    FROM
        orderdetails
    ORDER BY quantityOrdered * priceEach DESC;
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
