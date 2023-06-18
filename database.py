import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tf_prog_av"
)


mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

tables = mycursor.fetchall()

# Print the table names
for table in tables:
    print(table[0])