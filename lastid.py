import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="paindabad&786",
    database="mydatabase"
)

mycursor = mydb.cursor()

print("ID: ", mycursor.lastrowid)
