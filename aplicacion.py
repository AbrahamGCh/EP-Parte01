import os



def menu():
    print("\n\t\t\t  -------------------- ")
    print("\t\t\t |  MENU DE OPCIONES  |")
    print("\t\t\t  -------------------- \n")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")
    


def salir():
    print("Gracias por su visita....")

def error():
    print("Opción incorrecta")

login = open("usuarios.txt","rt")
leerLogin = login.read()
password = open("claves.txt","rt")
leerPassword = password.read()
intentos = 0
while intentos < 3:
    user = input("\n\tIngrese su usuario: ")
    clave = input("\tIngrese la clave: ")
    if user == leerLogin and clave == leerPassword:
        opcion = 1
        while True:
            menu()
            opcion = int(input("\nopcion: "))
            if opcion == 3:
                salir()
                break
            else:
                error()
        break  # Salir del bucle si las credenciales son correctas
    else:
        print("El usuario y/o clave es incorrecto\n")
        intentos += 1
        if intentos == 3:
            print("Número máximo de intentos alcanzado. Saliendo del programa.\n")
            break