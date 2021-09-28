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




if __name__ == '__main__':
    cadena = ingresar_datos.ingresar_letras("Ingrese una palabra")
    print(cadena)
    numero = ingresar_datos.ingresar_numeros_enteros("Ingrese un numero")
    print(numero)
