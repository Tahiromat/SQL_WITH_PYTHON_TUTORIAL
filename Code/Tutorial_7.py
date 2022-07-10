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

############ LIMIT ############ 
query = '''
	SELECT 
		customerNumber, customerName, creditLimit
	FROM
		customers
	ORDER BY creditLimit DESC
	LIMIT 5;
'''

############ LIMIT FOR PAGINATION ############ 
query = '''
	SELECT 
		customerNumber, customerName
	FROM
		customers
	ORDER BY customerName
	LIMIT 10 , 10;
'''

############ LIMIT OT GET n^th HIGHEST OR LOWEST VALUE ############ 
query = '''
	SELECT 
		customerName, creditLimit
	FROM
		customers
	ORDER BY creditLimit DESC
	LIMIT 1 , 1;
'''

############ LIMIT WITH DISTINCT ############ 
query = '''
	SELECT DISTINCT
		state
	FROM
		customers
	WHERE
		state IS NOT NULL
	LIMIT 5;
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