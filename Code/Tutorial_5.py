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

############ BETWEEN WITH NUMBERS ############ 
query = '''
    SELECT 
        productCode, productName, buyPrice
    FROM
        products
    WHERE
        buyPrice BETWEEN 90 AND 100;
'''

############ NOT BETWEEN ############ 
query = '''
	SELECT 
		productCode, productName, buyPrice
	FROM
		products
	WHERE
		buyPrice NOT BETWEEN 20 AND 100;
'''

############ BETWEEN WITH DATES ############ 
query = '''
	SELECT 
		orderNumber, requiredDate, status
	FROM
		orders
	WHERE
		requireddate BETWEEN CAST('2003-01-01' AS DATE) AND CAST('2003-01-31' AS DATE);
'''

############  ############ 
# query = '''

# '''

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