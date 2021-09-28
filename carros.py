class Carros:
   
    def __init__(self,marca,modelo,version,año,precio,status,propietario = "Age true"):
        self.__marca = marca
        self.__modelo = modelo
        self.__version = version
        self.__año = año
        self.__precio = precio
        self.__status = status
        self.__propietario = propietario
    
#######################################    
    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self,marca):
        print("Modificando valor")
        self.__marca = marca
#######################################
    @property
    def modelo(self):
        return self.__marca 
    @modelo.setter
    def modelo(self,modelo):
        print("Modificando valor")
        self.__modelo = modelo
########################################
    @property
    def version(self):
        return self.__version
    @version.setter
    def version(self,version):
        print("Modificando valor")
        self.__version = version
#########################################
    @property
    def año(self):
        return self.__año
    @año.setter
    def año(self,año):
        self.__año = año
        assert año > 1886, "ERROR AÑO DEL CARRO NO DISPONIBLE"
###########################################
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self,precio):
        self.__precio = precio
##########################################
    @property 
    def status(self):
        estados_de_venta= { 1:"Disponible", 0:"No Disponible"}
        return estados_de_venta[self.__status]
    @status.setter
    def status(self,status):
        self.__status = status
#########################################
    @property
    def propietario(self):
        return self.__propietario 
    @propietario.setter
    def propietario(self,propietario):
        self.__propietario = propietario
#############################################
    def mostrar_datos_del_vehiculo(self):
        print(f"""
Los datos del vehiculo son los siguientes
Marca: {self.__marca}
Modelo: {self.__modelo}
Version: {self.__version}
Año: {self.__año}
Precio: {self.__precio}
Status: {self.__status}
Propietario: {self.__propietario}        
        """)
        



    
    



#if __name__ == "__main__":
    # lista = []

    # arona = Carros("Seat","Arona","Style",2019,310000,1,"Age_True")

    
    


    
    