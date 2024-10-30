from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='', host='127.0.0.1', database='biblioteca')
cursor = cnx.cursor()
cursor.execute("SELECT * FROM libro;")
for registro in cursor:
    print(registro)
cnx.close()

# DESGRACIAU PROBLEMA