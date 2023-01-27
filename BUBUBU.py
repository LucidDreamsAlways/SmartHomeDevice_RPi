import datetime
import sqlite3

u = 124
p = 8493

year = 2022
days_in_year = (datetime.date(year+1, 1, 1) - datetime.date(year, 1, 1)).days
result = u + p * days_in_year
print(result)


# Create a connection to a SQLite database
conn = sqlite3.connect('customer_data.db')

# Create a table to store customer data
conn.execute('''CREATE TABLE CUSTOMERS
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL);''')

# Insert sample data into the table
conn.execute("INSERT INTO CUSTOMERS (ID,NAME,AGE) \
      VALUES (1, 'John Doe', 25)")
conn.execute("INSERT INTO CUSTOMERS (ID,NAME,AGE) \
      VALUES (2, 'Jane Smith', 32)")

# Commit the changes and close the connection
conn.commit()
conn.close()

v = 69
o = 420

lol = print v + o and * with current time


import datetime

v = 69
o = 420
current_time = datetime.datetime.now()

result = v + o * current_time.microsecond
print(result)

