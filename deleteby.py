import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="paindabad&786",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE name = 'mosh'"
mycursor.execute(sql)

mydb.commit()
