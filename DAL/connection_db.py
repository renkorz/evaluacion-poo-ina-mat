from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='', host='127.0.0.1', database='empresa_test')
cursor = cnx.cursor()
cursor.execute("SELECT * FROM client;")
for registro in cursor:
    print(registro)
cnx.close()

# DESGRACIAU PROBLEMA