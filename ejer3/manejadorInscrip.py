import numpy as np
from claseInscripcion import inscripcion
import csv
class ArregloInscripciones():
    def __init__(self,dimencion=1,incremento=4):
        self.__arreglo=np.empty(dimencion,dtype=inscripcion)
        self.__cantidad=0
        self.__dimencion=dimencion
        self.__incremento=incremento
    def agregar_arre_inscrip(self,dato):
        if(self.__cantidad == self.__dimencion):
            self.__dimencion+=self.__incremento
            self.__arreglo.resize(self.__dimencion)
        self.__arreglo[self.__cantidad]=dato
        self.__cantidad+=1
    def MOSTRARINSC(self):
        for insc in self.__arreglo:
            print(insc)
    def validarpago(self,i):
        self.__arreglo[i].setpago()
    def guardarArchivo(self):
        data = {}
        lista = []
        for inscripto in self.__arreglo:
            if inscripto != None:
                taller=inscripto.gettaller()
                persona=inscripto.getPersona()
                fecha=inscripto.getfecha()
                pago=inscripto.getpago()
                data={"dni":persona.getdni(),"IdTaller":taller.getid(),
                "FechaInscripcion":fecha,"Pago":pago}
                lista.append(data)
        print(lista)
        #archivo=open("inscripciones.csv","w")
        with open("inscripciones.csv","w") as archivo:
            nombres = ["dni","IdTaller","FechaInscripcion","Pago"]
            escribir = csv.DictWriter(archivo,fieldnames=nombres)
            escribir.writeheader()
            for datas in lista:
                escribir.writerow(datas)
           
