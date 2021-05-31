from Empleado import Empleados
class planta(Empleados):
    __SueldoBasico=None
    __Antiguedad=None
    def __init__ (self,dni,nom,dir,tel,sueldo,ant):
        super().__init__(dni,nom,dir,tel)
        self.__SueldoBasico = sueldo
        self.__Antiguedad = ant
    def getsuedo(self):
        return self.__SueldoBasico
    def setsueldo(self):
        self.__SueldoBasico+=25000
        return self.__SueldoBasico
    def pla(self):
        #Sueldo = sueldo básico+ 1% del sueldo básico*antigüedad
        sueldo=0
        sueldo= float(self.__SueldoBasico) + (float(self.__SueldoBasico)/100)* int(self.__Antiguedad)
        return sueldo
   