class Pelicula():
	__título:str
	__resumen:str
	__lenguaje:str
	__fecha:str
	def __init__(self, tit, res, leng, fecha):
		self.__título=tit
		self.__resumen=res
		self.__lenguaje=leng
		self.__fecha=fecha
		self.__genero=[]
	def carga_genero(self, genero):
		self.__genero.append(genero)
	def getTitulo(self):
		return self.__título
	def getResumen(self):
		return self.__resumen
	def getLenguaje(self):
		return self.__lenguaje
	def getFecha(self):
		return self.__fecha
	def getGenero(self):
		return self.__genero
