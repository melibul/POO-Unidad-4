from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from urllib.request import urlopen
import json
class Interfaz():
	__ventana:None
	def __init__(self):
		self.__ventana=Tk()
		self.__ventana.title('Conversor de Moneda')
		self.__ventana.configure(bg='gray83')
		self.__dolares=StringVar()


		self.mainframe=Frame()
		self.mainframe.pack()
		self.mainframe.configure(bg='gray83')

		Label(self.mainframe, text='dólares', background='gray83').grid(column=3, row=0, sticky=W)
		Label(self.mainframe, text='es equivalente a', background='gray83').grid(column=1, row=1, sticky=W)
		Label(self.mainframe, textvariable=self.__dolares, background='gray83').grid(column=2, row=1, sticky=W)
		Label(self.mainframe, text='pesos', background='gray83').grid(column=3, row=1,sticky=W)

		self.plata=Entry(self.mainframe,bg='white', width=8)
		self.plata.grid(column=2, row=0, sticky=W)


		Button(self.mainframe, text='Salir', background='gray71', command=self.__ventana.destroy, width=10).grid(column=2, row=2, padx=10, pady=10)
		Button(self.mainframe, text='Calcular', background='gray71', command=self.calcular, width=10).grid(column=1, row=2, padx=10, pady=10)
		

		url = "https://www.dolarsi.com/api/api.php?type=dolar"
		response = urlopen(url)
		self.data = json.loads(response.read())
		self.__ventana,mainloop()

	def calcular(self):
		try:
			cotizacion=self.data[0]['casa']['venta']
			cotizacion=cotizacion.replace(',','.')
			dolar=float(self.plata.get())* float(cotizacion)
			self.__dolares.set(dolar)

		except ValueError:
			messagebox.showerror(title='Error', message='Debe ingresar un valor numerico en la casilla')
if __name__ == '__main__':
	mi_app=Interfaz()