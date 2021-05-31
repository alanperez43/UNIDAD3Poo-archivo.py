class ManejaHelados (object):
    def __init__ (self):
        self.__lista = []
    
    def AgregarHelado (self,Helado):
        self.__lista.append(Helado)

    def Item2Mostrar (self,numero):
        numeros={}
        for i in range (1,numero+1):
            numeros[i]=0
        for helado in self.__lista:
            sabores=helado.getSabor()
            for sabor in sabores:
                numero=sabor.getNumero()
                numeros[numero]+=1
        dicOrdenado=sorted(numeros.items(),key=lambda x:x[1],reverse=True)
        lista5populares=[]
        if(len(dicOrdenado)>5):
            lista5populares=dicOrdenado[0:5]
        else:
            lista5populares=dicOrdenado
        return lista5populares
    
    def saboresvendidos (self):
        for sabor in self.__lista:
            nombre = sabor.getSabor()
            for nom in nombre:
                print(nom.getNombre())
