from manejadorLibros import manejador
from clase_menu import Menu
if __name__ == "__main__":
    listar=manejador()
    listar.cargar("libros.csv")
    listar.mostrar()
    menu=Menu()
    op=None
    while(op!=4):
        print("|------------------------------------------------------|")
        print("|1 para:Ingresar el identificador de un libro y mostrar|")
        print("|2 para:Dada una palabra, mostrar                      |")
        print("|3 para:test                                           |")
        print("|------------------------------------------------------|")
        op=int(input("ingresar opcion: "))
        menu.opcion(op,listar)