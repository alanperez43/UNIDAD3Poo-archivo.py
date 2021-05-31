class inscripcion():
    __fechaiscripcion=None
    __pago=None
    __taller=None
    __persona=None
    def __init__(self,fecha,persona,taller,pago=False):
        self.__fechaiscripcion=fecha
        self.__pago=pago
        self.__taller=taller
        self.__persona=persona
    def __str__(self):
        s="\nfecha :{}".format(self.__fechaiscripcion)
        s+="\npago :{}".format(self.__pago)
        s+="\ntaller :{}".format(self.__taller)
        s+="\npersona :{}".format(self.__persona)
        s+="\n"
        return s
    def getfecha(self):
        return self.__fechaiscripcion
    def getpago(self):
        return self.__pago
    def gettaller(self):
        return self.__taller
    def getPersona(self):
        return self.__persona
    def setpago(self):
        print("VALOR SIN MODIFICAR")
        print(self.__pago)
        self.__pago=True
        print("VALOR MODIFICADO")
        print(self.__pago)