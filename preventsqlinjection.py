import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="paindabad&786",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Highway 21", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()


print(mycursor.rowcount, "record(s) affected")
