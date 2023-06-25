class Imaginario:
    def __init__(self,oper=0,operim=0):
        self.__oper=oper
        self.__operim=operim
    
    def get_oper(self):
        return self.__oper
    def get_operim(self):
        return self.__operim
    
    def __add__(self,otro):
        self.__oper+=otro.get_oper()
        self.__operim+=otro.get_operim()
        if self.__operim<0:
            resul="{}{}i".format(self.__oper,self.__operim)
        else:
            resul="{}+{}i".format(self.__oper,self.__operim)
        return resul
    
    def __sub__(self,otro):
        self.__oper-=otro.get_oper()
        self.__operim-=otro.get_operim()
        if self.__operim<0:
            resul="{}{}i".format(self.__oper,self.__operim)
        else:
            resul="{}+{}i".format(self.__oper,self.__operim)
        return resul
    
    def __mul__(self,otro):
        oper=(self.__oper*otro.get_oper()- self.__operim*otro.get_operim())
        operim=(self.__oper*otro.get_operim()+self.__operim*otro.get_oper())
        self.__oper=oper
        self.__operim=operim
        if self.__operim<0:
            resul="{}{}i".format(self.__oper,self.__operim)
        else:
            resul="{}+{}i".format(self.__oper,self.__operim)
        return resul
    
    def __truediv__(self,otro):
        oper=(self.__oper*otro.get_oper()+self.__operim*otro.get_operim())/(otro.get_oper()*otro.get_oper()+otro.get_operim()*otro.get_operim())
        operim=(self.__operim*otro.get_oper()-self.__oper*otro.get_operim())/(otro.get_oper()*otro.get_oper()+otro.get_operim()*otro.get_operim())
        self.__oper=oper
        self.__operim=operim
        if self.__operim<0:
            resul="{}{}i".format(self.__oper,self.__operim)
        else:
            resul="{}+{}i".format(self.__oper,self.__operim)
        return resul
    
    def __str__(self):
        return "{}+{}i".format(self.__oper,self.__operim)
