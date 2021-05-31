class Capitulo:
    __Titulo=None 
    __CantidadPaginas=None
    def __init__(self,titulo,cant):
        self.__Titulo=titulo
        self.__CantidadPaginas=cant
    def gettitulo(self):
        return self.__Titulo
    def getcantidad(self):
        return self.__CantidadPaginas
    