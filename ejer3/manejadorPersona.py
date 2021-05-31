from clasePersona import Persona
from manejadorTalleres import Arreglo
class Mpersona():
    __listaP=[]
    def __init__(self):
        self.__listaP=[]
    def agregarP(self,persona):
        self.__listaP.append(persona)
    def mostrarpersona(self):
        
        for persona in self.__listaP:
            print(persona)
    def buscardni(self,ManejaTalleres,dni,id):
        i=0
        while (i < len(self.__listaP) and dni != int(self.__listaP[i].getdni())):
            i+=1
            
        if(i < len(self.__listaP)):
            print("DNI VALIDO")
            ManejaTalleres.listar(id) 
    def modifica(self,ManejaInsc,dni):
        i=0
        while (i < len(self.__listaP) and dni != int(self.__listaP[i].getdni())):
            i+=1
        if(i < len(self.__listaP)):
            ManejaInsc.validarpago(i)

            
