import mysql.connector

## Now connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="904724"
)

print(mydb)