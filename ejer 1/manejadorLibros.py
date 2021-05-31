import csv
from libro import libros
from capitulo import Capitulo
class manejador:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def cargar(self,archivo):
        
        libro=open(archivo)
        reader=csv.reader(libro,delimiter=";")
        for i in reader:
            if len(i)==6:
                libroz=libros(int(i[0]),i[1],i[2],i[3],int(i[4]),i[5])
                self.__lista.append(libroz)  
            else:
                libroz.agregarcap(Capitulo(i[0],int(i[1])))
        libro.close()
    def mostrar(self):
        for libro in self.__lista:
            print(libro)
    def buscar(self,id):
        i=0
        #for libro in self.__lista:
        while(i<len(self.__lista) and id != int(self.__lista[i].getid())):
            i+=1
        if (i<len(self.__lista)):
            return i
        else:
            return -1   
    def item1(self,id):
        print("titulo {}".format(self.__lista[id].gett()))
        print("-----CAPITULOS-----")
        self.__lista[id].cap()
        '''cap=self.__lista[id].getcap()
        total=0
        i=1
        for libro in cap:
            print("Nombre del Capitulo {}:{}\n".format(i,libro.gettitulo()))
            i+=1
            total=total+libro.getcantidad()
        print("Cantidad total de paginas:",total)'''
    def item2(self,palabra):
        for libro in self.__lista:
            if (libro.gett().lower().count(palabra)!=0):
                print(libro.gett() ,"de", libro.getautor())
                print("\n")
                id=libro.getid()
                autor=str(libro.getautor())
                self.__lista[id-1].cap2(palabra,autor)
        