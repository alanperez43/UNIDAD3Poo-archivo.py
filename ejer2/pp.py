from ClaseHelado import Helado
from ClaseSabor import Sabor
from ManejadorHelados import ManejaHelados
from ManejadorSabores import ManejaSabores
from claseMenu import Menu
import csv,os
if __name__ == "__main__":
    
    archivo = open("sabores.csv")
    leer = csv.reader(archivo, delimiter=";")
    Mansabor = ManejaSabores()
    manejaHelado = ManejaHelados()
    for sabor in leer:
        Mansabor.addSabor(Sabor(int(sabor[0]),sabor[1],sabor[2]))
    archivo.close()
    opcion = None
    menu=Menu()
    while opcion != 5:
        print("|------------------------------------------------------------|")
        print("| Ingrese 1 para registrar una venta de helado               |")
        print("| Ingrese 2 para ver el nombre de los 5 sabores mas pedidos  |")
        print("| Ingrese 3 para estimar los gramos vendidos                 |")
        print("| Ingrese 4 para mostrar los sabores vendidos un tamaño dado |")
        print("| Ingrese 5 para cerrar programa                             |")
        print("|------------------------------------------------------------|")
        opcion = int(input("Ingrese Opcion: "))
        menu.opcion(opcion,Mansabor,manejaHelado) 
     