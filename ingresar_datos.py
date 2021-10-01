from typing import TextIO


class ingresar_datos:


    def ingresar_letras(texto):
        cadena = input(texto)
        return cadena
    
    def ingresar_numeros_enteros(texto):
        while True:
            try:
                numero = int(input(texto))
                return numero
                break
            except ValueError:
                print("!!!!!!ERROR SOLO SE PUEDEN INGRESAR NUMEROS ENTEROS¡¡¡¡¡¡")
    
    def ingresar_numeros_decimales(texto):
        while True:
            try:
                numero = float(input(texto))
                return numero
                break
            except ValueError:
                print("!!!!!!ERROR SOLO SE PUEDEN INGRESAR NUMEROS¡¡¡¡¡¡")
    
    def ingresar_1_o_0(texto):
        while True:
            try:
                numero = int(input(texto))
                try:
                    if numero == 1:
                        return True
                    elif numero == 0:
                        return False
                    else:
                        raise ValueError("!!!!!!ERROR SOLO SE PUEDEN INGRESAR NUMEROS MAYORES A UNO¡¡¡¡¡¡")
                except ValueError as solo_binarios:
                    print(solo_binarios)

            except ValueError:
                print("!!!!!!ERROR SOLO SE PUEDEN INGRESAR NUMEROS¡¡¡¡¡¡")






# if __name__ == '__main__':
#     cadena = ingresar_datos.ingresar_letras("Ingrese una palabra")
#     print(cadena)
#     numero = ingresar_datos.ingresar_numeros_enteros("Ingrese un numero")
#     print(numero)
#     numero_2 = ingresar_datos.ingresar_numeros_decimales("Ingresar numero con decimales: ")
#     print(numero_2)
#     binario = ingresar_datos.ingresar_1_o_0("Ingresar un 1 o 0")
#     print(binario)

