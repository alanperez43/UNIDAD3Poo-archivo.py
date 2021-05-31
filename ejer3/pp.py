from manejadorTalleres import Arreglo
from claseTaller import Taller
from clasePersona import Persona
from manejadorPersona import Mpersona
from manejadorInscrip import ArregloInscripciones
import csv
if __name__ == "__main__":
    archivo = open("Talleres.csv")
    leer = csv.reader(archivo, delimiter=";")
    bandera = 0
    ban=0
    for taller in leer:
        if len(taller) != 0:
            if bandera == 0:
                bandera = 1
            else:
                if(ban==0):
                    ManejaTalleres = Arreglo(int(taller[0]))
                    ban=1
                else:
                    talleres = Taller(int(taller[0]),taller[1],int(taller[2]),int(taller[3]))
                    ManejaTalleres.AgregarTaller(talleres)
        else:
            print("Se produjo un error en el archivo CSV")
    archivo.close()
    ManejaPersonas=Mpersona()
    ManejaInsc=ArregloInscripciones()
    print("REALIZAR UNA INCRIPCION")
    Nombre=str(input("ingresar nombre: "))
    direccion=str(input("ingresar su direccion: "))
    dni=input("ingresar su dni: ")
    persona=Persona(Nombre,direccion,dni)
    ManejaPersonas.agregarP(persona)
    print("para registrar fecha")
    año=input("ingresar año precente: ")
    mes=input("ingresar mes precente: ")
    dia=input("ingresar dia precente: ")
    decha_de_inscripcion=str(dia)+"/"+str(mes)+"/"+str(año)
    print("Seleccionar taller a inscrubir")
    ManejaTalleres.Mostrar()
    id=int(input(""))
    i=ManejaTalleres.buscar(id)
    while i == -1:
        print("seleccion no calida,vuelva a seleccionar un taller")
        id=int(input(""))
        i=ManejaTalleres.buscar(id)
    print("dato valido")
    objeto=ManejaTalleres.registrar(decha_de_inscripcion,persona,i)
    ManejaInsc.agregar_arre_inscrip(objeto)
    
    print("MOSTRAR INSCRIPCIONES")
    ManejaInsc.MOSTRARINSC()
    print("******item3******")
    dni=int(input("Ingresar dni para mostrar Taller + monto adeudado: "))
    ManejaPersonas.buscardni(ManejaTalleres,dni,id)
    print("******item4******")
    id=int(input("ingresar id para listar:"))
    ManejaTalleres.item4(id,ManejaPersonas)
    print("******item5******")
    #print("MOSTRAR PERSONAS")
    #ManejaPersonas.mostrarpersona()
    dni=int(input("Ingresar dni para pagar monto adeudado: "))
    ManejaPersonas.modifica(ManejaInsc,dni)
    print("******item6******")
    ManejaInsc.guardarArchivo()
    print("FIN DEL PROGRAMA, ARCHIVO GUARDADE")