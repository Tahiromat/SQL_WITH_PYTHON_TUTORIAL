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

############ LIKE ############ 
query = '''
	SELECT 
		employeeNumber, lastName, firstName
	FROM
		employees
	WHERE
		firstName LIKE 'a%';
'''

############ LIKE CONTAIN ############ 
query = '''
	SELECT 
		employeeNumber, firstName, lastName
	FROM
		employees
	WHERE
		lastName LIKE '%on%';
'''

############ LIKE WITH UNDERSCORE(_) ############ 
query = '''
	SELECT 
		employeeNumber, firstName, lastName
	FROM
		employees
	WHERE
		firstname LIKE 'T_m';
'''

############ NOT LIKE ############ 
query = '''
	SELECT 
		employeeNumber, firstName, lastName
	FROM
		employees
	WHERE
		lastName NOT LIKE 'B%';	
'''

############ LIKE WITH ESCAPE ############ 
query = '''
	SELECT 
		productCode, productName
	FROM
		products
	WHERE
		productCode LIKE '%$_20%' ESCAPE '$';
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