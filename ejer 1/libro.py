class libros():
    __idlibro=None
    __titulo=None
    __autor=None
    __editorial=None
    __isbn=None
    __cantidadCapitulos=None
    __capitulo=None
    def __init__(self,id,titulo,autor,edit,isbn,cant):
        self.__idlibro=id
        self.__titulo=titulo
        self.__autor=autor
        self.__editorial=edit
        self.__isbn=isbn
        self.__cantidadCapitulos=cant
        self.__capitulo=[]
    def agregarcap(self,algo):
        self.__capitulo.append(algo)
    def getid(self):
        return self.__idlibro
    def gett(self):
        return self.__titulo
    def getautor(self):
        return self.__autor
    def cap(self):
        total=0
        i=1
        print("jas")
        for libro in self.__capitulo:
            print("hola")
            print("Nombre del Capitulo {}:{}\n".format(i,libro.gettitulo()))
            i+=1
            total=total+libro.getcantidad()
        print("Cantidad total de paginas:",total)
    def cap2(self,palabra,autor):
        for capitulo in self.__capitulo:
            if (capitulo.gettitulo().lower().count(palabra)!=0):
                print(capitulo.gettitulo(),"capitulo de autor",autor)
                print("\n")
    def __str__(self):
        s = "\nId de libro: {} ".format(self.__idlibro)
        s += "\nTitulo: {} " .format(self.__titulo)
        s += "\nAutor: {}" .format(self.__autor)  
        s += "\nEditorial: {}" .format(self.__editorial)
        s += "\nisbn: {} " .format(self.__isbn)
        s += "\nCantidad de campitulos: {}" .format(self.__cantidadCapitulos) 
        s += "\n**************** CAPITULOS ****************"
        acum=0
        for i in self.__capitulo:
            s +="\n{}" .format(i.gettitulo())
            s +="\n{}" .format(i.getcantidad())
            s += "\n"
        return s