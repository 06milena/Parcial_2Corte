from models import users

def listarBases(datos):
    print('recibido')
    bases=users.listar(datos)
    return bases

