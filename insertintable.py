import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="paindabad&786",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Mosh", "Centeral 30")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")
