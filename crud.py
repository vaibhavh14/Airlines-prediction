import pymysql

#connect to the database server

import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Insha@12",
        database="flights"
    )

    cursor = connection.cursor()
    print("Connected to MySQL successfully")

except Exception as e:
    print("Connection error:", e)

