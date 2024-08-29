import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    name = 'root',
    passwd = 'nikhil',
)

# Prepare the cursor object 

cursorObject  = database.cursor()

cursorObject.execute('CREATE DATABASE websiteDB')

print('All Done!')