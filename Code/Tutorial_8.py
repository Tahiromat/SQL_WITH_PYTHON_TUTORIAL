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

############ ALIAS FOR COLUMNS ############ 
query = '''
	SELECT 
		CONCAT_WS(', ', firstname, lastName) AS `Full name`
	FROM
		employees
	ORDER BY `Full name`;
'''

############ ALIAS WITH GROUP BY AND HAVING ############ 
query = '''
    SELECT 
        orderNumber `Order no.`,
        SUM(priceEach * quantityOrdered) total
    FROM
        orderdetails
    GROUP BY `Order no.`
    HAVING total > 60000;
'''

############ ALIAS FOR TABLES ############ 
query = '''
	SELECT 
		e.firstName, e.lastName
	FROM
		employees e
	ORDER BY e.firstName; 
'''

############ WHEN BOTH TABLES HAVE THE SAME COLUMN NAME ############ 
query = '''
	SELECT 
		customerName, COUNT(o.orderNumber) total
	FROM
		customers c
			INNER JOIN
		orders o ON c.customerNumber = o.customerNumber
	GROUP BY customerName
	ORDER BY total DESC;
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