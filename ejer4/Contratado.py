from Empleado import Empleados
class contratado(Empleados):
    __FechaInicio=None
    __FechaFin=None
    __cant_horas=None
    __ValorPorHora=None
    def __init__(self,dni,nom,dir,tel,FI,FF,CH,CPH):
        super().__init__(dni,nom,dir,tel)
        self.__FechaInicio=FI
        self.__FechaFin=FF
        self.__cant_horas=CH
        self.__ValorPorHora=CPH
    def gethoras(self):
        return self.__cant_horas
    def sethoras(self,algo):
        self.__cant_horas+=algo
        return self.__cant_horas
    def con(self):
        #Sueldo = cantidad de horas trabajadas * valor de la hora
        sueldo=0
        sueldo= int(self.__cant_horas) * float(self.__ValorPorHora)
        return sueldo