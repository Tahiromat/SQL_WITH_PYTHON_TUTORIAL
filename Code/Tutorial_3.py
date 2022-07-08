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

############ WHERE WITH EQUALITY ############ 
query = '''
    SELECT 
        firstname, lastname, jobtitle
    FROM
        classicmodels.employees
    WHERE
        jobtitle = 'Sales Rep';
'''

############ WHERE WITH AND OPERATOR ############ 
query = '''
    SELECT 
        lastname, firstname, jobtitle, officeCode
    FROM
        classicmodels.employees
    WHERE
        jobtitle = 'Sales Rep'
            AND officeCode = 1;
'''

############ WHERE WITH OR OPERATOR ############ 
query = '''
    SELECT 
        lastName, firstName, jobTitle, officeCode
    FROM
        classicmodels.employees
    WHERE
        jobtitle = 'Sales Rep' OR officeCode = 1
    ORDER BY officeCode , jobTitle;
'''

############ WHERE WITH LIKE  OPERATOR ############ 
query = '''
    SELECT 
        firstName, lastName
    FROM
        classicmodels.employees
    WHERE
        lastName LIKE '%son'
    ORDER BY firstName;
'''

############ WHERE WITH IN  OPERATOR ############ 
query = '''
    SELECT 
        firstName, lastName, officeCode
    FROM
        classicmodels.employees
    WHERE
        officeCode IN (1 , 2, 3)
    ORDER BY officeCode;
'''

############ WHERE WITH IS NULL OPERATOR ############ 
query = '''
    SELECT 
        lastName, firstName, reportsTo
    FROM
        classicmodels.employees
    WHERE
        reportsTo IS NULL;
'''

############ WHERE WITH COMPARISON OPERATORS ############ 
query = '''
    SELECT 
        firstname, lastname, officeCode
    FROM
        classicmodels.employees
    WHERE
        officecode > 5;
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