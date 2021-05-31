from claseTaller import Taller
from claseInscripcion import inscripcion
import numpy as np
class Arreglo ():
    def __init__ (self,dimencion=1,incremento=4):
        self.__array = np.empty(dimencion,dtype=Taller)
        self.__cantidad = 0
        self.__dimencion = dimencion
        self.__incremento = incremento

    def AgregarTaller (self,taller):
        if self.__cantidad == self.__dimencion:
            self.__dimencion += self.__incremento
            self.__array.resize(self.__dimencion)
        self.__array[self.__cantidad]=taller
        self.__cantidad += 1
    def Mostrar(self):
        print("{}       {}       {}       {}".format("NumTaller","Nombre del taller","Vacantes","Monto"))
        for taller in self.__array:
            print(taller)
    def buscar(self,id):
        i=0
        while((i < len(self.__array))and(id != self.__array[i].getid())):
            i+=1
        if(i < len(self.__array)):
            return i
        else:
            return -1
    def registrar(self,fecha,persona,id):
        if(self.__array[id].getvacantes()>0):
            inscrip=inscripcion(fecha,persona,self.__array[id]) 
            self.__array[id].agregar(inscrip)
            return inscrip
        else:
            print("no hay vacantes en este taller")   
    def listar(self,indice):
        
        print("Taller {} mas monto adeudado {} ".format(self.__array[indice-1].getTaller(),self.__array[indice-1].getMonto()))
    def item4(self,id,ManejaPersonas):
        busca=self.buscar(id)
        if(busca ==-1):
            print("elemento no valido")
        self.__array[busca].acceder()
        #print(self.__array[busca])
        #ManejaPersonas.listaitem4(busca)
   