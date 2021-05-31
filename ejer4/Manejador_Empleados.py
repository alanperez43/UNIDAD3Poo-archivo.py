import numpy as np
import csv
from Contratado import contratado
from Externo import externo
from Planta import planta
from Empleado import Empleados
from datetime import datetime
class ManejadorEmpleados():
    
    def __init__(self,dimencion=10):
        self.__arreglo=np.empty(dimencion,dtype=Empleados)
        self.__cantidad=0
        self.__dimencion=dimencion
        
    def cargar(self,algo):
        if self.__cantidad < self.__dimencion:
            self.__arreglo[self.__cantidad]=algo
            self.__cantidad+=1

    def coleccion(self):
        archivo1=open("contratados.csv")
        archivo2=open("externos.csv")
        archivo3=open("planta.csv")
        leer1=csv.reader(archivo1,delimiter=";")
        leer2=csv.reader(archivo2,delimiter=";")
        leer3=csv.reader(archivo3,delimiter=";")
        ban=1

        for con in leer1:
            if (ban==1):
                ban=0
            else:
                a=contratado(con[0],con[1],con[2],con[3],con[4],con[5],int(con[6]),con[7])
                self.cargar(a)    
        for ext in leer2:
            if(ban==0):
                ban=1
            else:
                self.cargar(externo(ext[0],ext[1],ext[2],ext[3],ext[4],ext[5],ext[6],ext[7],ext[8],ext[9]))
            
        for pla in leer3:
            if(ban==1):
                ban=0
            else:
                self.cargar(planta(pla[0],pla[1],pla[2],pla[3],float(pla[4]),int(pla[5])))
        archivo1.close()
        archivo2.close()
        archivo3.close()
    def buscar(self,dni):
        i=0
        while (i < len(self.__arreglo) and dni != int(self.__arreglo[i].getdni())):
            i+=1
        if(i < len(self.__arreglo)):
            return i
        else:
            return -1
    def item1(self,dni,hora):
        indice=self.buscar(dni)
        if(indice != -1):
            if isinstance(self.__arreglo[indice],contratado):
                print("Cantidad de horas del empleado {}".format(self.__arreglo[indice].gethoras()))
                print("Horas Reguistradas {}".format(self.__arreglo[indice].sethoras(hora)))
            else:
                print("error")
        else:
            print("dni no valido")
    def item2(self,tarea):
        año=input("Año actual: ")
        mes=input("mes actual: ")
        dia=input("dia actual: ")
        Fecha_Actual = str(dia)+"/"+str(mes)+"/"+str(año)
        acum=0
        for empleados in self.__arreglo:
            if isinstance(empleados,externo):
                #print("lo que retorna gettarea",empleados.gettarea().lower())
                #print("tarea",tarea.lower())
                #if (str(empleados.gettarea()).lower()==tarea.lower()):
                ta=str(empleados.gettarea()).lower()
                print(ta)
                tarea=tarea.lower()
                if (tarea == ta):
                    if (str(Fecha_Actual) > str(empleados.gethora())):
                        print("hola2",empleados.gethora())
                        print("hola3")
                        acum+=float(empleados.getcosto()) 
        print("Para la tarea",tarea,"El monto total a pagar es",acum)
    def item3(self):
        for pla in self.__arreglo:
            if isinstance(pla,planta):
                print(int(pla.getsuedo()))
                #sueldo=int(pla.getsuedo())
                if pla.getsuedo() < 2500:
                    print("Nombre",pla.getnombre())
                    print("Sueldo",pla.getsuedo())
                    print("DNI",pla.getdni())
                    print("Direccion",pla.getdireccion())
                    #pla.setsueldo()
                    print("Sueldo + ayuda",pla.getsuedo())
    def item4(self):
        for dato in self.__arreglo:
            if isinstance(dato,contratado):
                print("-------------------------")
                print("Nombre",dato.getnombre())
                print("DNI",dato.getdni())
                print("Sueldo",dato.con())
                print("-------------------------")
            if isinstance(dato,externo):
                print("-------------------------")
                print("Nombre",dato.getnombre())
                print("DNI",dato.getdni())
                print("Sueldo",dato.ext())
                print("-------------------------")
            if isinstance(dato,planta):
                print("Nombre",dato.getnombre())
                print("DNI",dato.getdni())
                print("Sueldo",dato.pla())
                print("-------------------------")

        
        

    

