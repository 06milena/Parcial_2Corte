import mysql.connector

def listar(datos):
    print('dTIAa')
    print(datos)
    DB= mysql.connector.connect(
        host=datos['host'],
        user=datos['users'],
        password=datos['contrasena'],
        port=datos['port']
    )

    cursor= DB.cursor(dictionary=True)
    cursor.execute('show databases;')
    return cursor.fetchall()




