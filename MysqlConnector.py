import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "1234", database = "Students")
mycursor = mydb.cursor()
mycursor.execute("select * from studentDetails")

#result = mycursor.fetchall()
#result = mycursor.fetchone()
#for row in result:
for i in mycursor:
    print(i)