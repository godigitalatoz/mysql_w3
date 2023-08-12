import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="paindabad&786",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(50), address VARCHAR(50))")
