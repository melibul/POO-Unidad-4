from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
class Interfaz():
	__ventana:None
	def __init__(self):
		self.__ventana=Tk()
		self.__ventana.configure(bg='gray83')
		self.__ventana.title('Calculo de IVA')
		self.__total=StringVar()
		
		self.mainframe=Frame()
		self.mainframe.pack()
		self.mainframe.configure(bg='gray83')

		
		Label(self.mainframe, text='Precio sin IVA').grid(column=0, row=0, padx=10, pady=10)
		self.precioBase=Entry(self.mainframe, bg='white')
		self.precioBase.grid(column=1, row=0, padx=10, pady=10)
		self.seleccion=BooleanVar()
		
		ttk.Radiobutton(self.mainframe, text='IVA 21%', value=0, variable=self.seleccion).grid(row=2, column=0, sticky='w')
		ttk.Radiobutton(self.mainframe, text='IVA 10.5%',value=1, variable=self.seleccion).grid(row =3, column=0,sticky='w')

		Label(self.mainframe, text='IVA').grid(column=0, row=4)
		Label(self.mainframe,text='', width=17, background='white').grid(column=1,row=4)
		Label(self.mainframe, text='Precion con IVA', background='white').grid(column=0, row=5, padx=10, pady=10)
		Label(self.mainframe,text='',width=17, background='white').grid(column=1,row=5)

		self.botonframe=Frame()
		self.botonframe.pack()
		self.botonframe.configure(bg='gray83')

		Button(self.botonframe, text='Calcular', command=self.calcularPrecio_IVA, background='gray54').grid(column=1, row=0, padx=50, pady=10)
		Button(self.botonframe, text='Salir', command=self.__ventana.destroy, background='IndianRed1').grid(column=2, row=0, padx=50, pady=10)
		self.__ventana.mainloop()
	def calcularPrecio_IVA(self):
		try:
			if self.seleccion.get()==0:
				iva=float((float(self.precioBase.get()))*(21/100))
				self.__total=float(iva)+float(self.precioBase.get())
				iva='$'+str(iva)
				self.__total='$'+str(self.__total)
			else: 
				iva=float((float(self.precioBase.get()))*(10.5/100))
				self.__total=float(iva)+float(self.precioBase.get())
				iva='$'+str(iva)
				self.__total='$'+str(self.__total)
			ttk.Label(self.mainframe, text=self.__total).grid(column=1, row=5, padx=10, pady=10)
			ttk.Label(self.mainframe, text=iva, background='white').grid(column=1, row=4, padx=10, pady=10)

		except ValueError:
			messagebox.showerror(title='Error', message='Debe ingresar un valor numerico en la casilla')
	
			
		
		
if __name__ == '__main__':
	mi_app=Interfaz()
