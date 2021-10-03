from ingresar_datos import *
from  carros import *

vehiculos = []

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
            elif menu == 4:
                exit()
            else:
                raise ValueError("!!!!!!ERROR OPCION NO VALIDA¡¡¡¡¡¡")
        except ValueError as e:
            print(e)



def altas_de_usuarios():
    print("Bienvenido al sistema de alta de usuarios")
    marca_carro = ingresar_datos.ingresar_letras("Ingrese la marca del carro: ")
    nombre_carro = ingresar_datos.ingresar_letras("Ingrese el nombre del carro:")
    version_carro = ingresar_datos.ingresar_letras("Ingrese la version del carro: ")
    año_carro = ingresar_datos.ingresar_numeros_enteros("Ingrese el año del carro: ")
    precio_carro = ingresar_datos.ingresar_numeros_decimales("Ingrese el precio del carro: ")
    status_carro = ingresar_datos.ingresar_1_o_0("Ingrese 1 si esta disponible y 0 si no esta disponible")
    vehiculos.append(Carros(marca_carro,nombre_carro,version_carro,año_carro,precio_carro,status_carro))
    print(vehiculos)
    print("VEHICULO DADO DE ALTA")
    Carros.mostrar_datos_del_vehiculo(vehiculos[-1])
    # with open("./archivos/vehiculos.txt","a") as f:
    #     f.write(Carros.mostrar_datos_del_vehiculo(vehiculos[-1]))
    #     f.write("\n")
    # vehiculos.clear()

    
    main()

    

  

def baja_de_usuarios():
    i = 0
    for vehiculo in vehiculos:
        i +=1
        print(f"Vehiculo numero: {i}")
        Carros.mostrar_datos_del_vehiculo(vehiculo)
    eliminar = ingresar_datos.ingresar_numeros_enteros("Ingrese el numero que deseas eliminar: ")
    vehiculos.pop(eliminar-1)
    main()

def consultar_usuarios():
    # with open("./archivos/vehiculos.txt","a") as f:
    #     for line in f:
    #         vehiculos.append(line)
    for vehiculo in vehiculos:
        Carros.mostrar_datos_del_vehiculo(vehiculo)
    main()






if __name__ == '__main__':
    main()