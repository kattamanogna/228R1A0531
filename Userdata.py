import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="12345", database="customerdata")
mycursor = conn.cursor()
if(mycursor):
    print("sucess")
else:
    print("problem")
query='insert into user(username,password,email,mobile_no)values(%s,%s,%s,%d)'
mycursor.execute(query)