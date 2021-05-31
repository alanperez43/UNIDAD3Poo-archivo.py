from manejadorLibros import manejador
class Menu:
    __menu=None
    def __init__(self):
        self.__menu={
            1:self.op1,
            2:self.op2,
            #3:self.op3,
        }
    def opcion(self,op,listar):
        func=self.__menu.get(op,lambda:print("opcion no valida"))
        if(op<1 or op>3):
            func()
        else:
            func(listar)
    def op1(self,listar):
        id=int(input("ingresar id :"))
        if(type(id)!=int):
            print("ingresar nuevamente,esta vez un numero entero")
            id=input("ingresar id :")
        indice=listar.buscar(id)
        print(indice)
        if (indice!=-1):
            listar.item1(indice)
        else:
            print("ERROR")
    def op2(self,listar):
        palabra=(input("Ingresar palabra a buscar y mostrar: "))
        if(type(palabra)!=str):
            print("ERROR DE TIPO ingresar nuevamete")
            palabra=(input("Ingresar palabra a buscar y mostrar: "))
        listar.item2(palabra)
