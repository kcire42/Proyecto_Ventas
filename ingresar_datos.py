class ingresar_datos:


    def ingresar_letras(texto):
        cadena = input(texto)
        return cadena
    
    def ingresar_numeros(texto):
        
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print("!!!!!!ERROR SOLO SE PUEDEN INGRESAR NUMEROS¡¡¡¡¡¡")





if __name__ == '__main__':
    cadena = ingresar_datos.ingresar_letras("Ingrese una palabra")
    print(cadena)
    numero = ingresar_datos.ingresar_numeros("Ingrese un numero")
    print(numero)
