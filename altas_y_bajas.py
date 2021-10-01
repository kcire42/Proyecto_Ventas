from ingresar_datos import *
from  carros import *


def main():
    while True:
        print("bienvenido a la alta de vehiculos")
        print("""
1- Dar de alta un usuario
2- Dar de baja un usuatio
3- Consultar usuarios
    """)
        menu = ingresar_datos.ingresar_numeros_enteros("Ingrese la opcion deseada: ")
        try:
            if menu == 1:
                altas_de_usuarios()
                break
            elif menu == 2:
                baja_de_usuarios()
                break
            elif menu == 3:
                consultar_usuarios()
                break
            else:
                raise ValueError("!!!!!!ERROR OPCION NO VALIDA¡¡¡¡¡¡")
        except ValueError as e:
            print(e)



def altas_de_usuarios():
    print("Bienvenido al sistema de alta de usuarios")
    vehiculos = []


  

def baja_de_usuarios():
    pass

def consultar_usuarios():
    pass






if __name__ == '__main__':
    main()