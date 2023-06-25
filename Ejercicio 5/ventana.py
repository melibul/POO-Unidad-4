import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from controlador import *
from modelo import *
import tkinter.font as tkFont



class Ventana():
	__ventana:None
	def __init__(self, manejador):
		self.__ventana=Tk()
		self.__ventana.title('Cartelera del Cine')
		self.__ventana.configure(bg='beige')

		fuente=tkFont.Font(family="Bookman Old Style",size= "12",weight="bold")
		frame_izquierdo=Frame()
		frame_izquierdo.pack(side='left')
		frame_izquierdo.configure(bg='beige')

		self.barra=tk.Scrollbar(frame_izquierdo)
		
		fuente2=tkFont.Font(family="Bookman Old Style",size= "16",weight="bold")

		Label(frame_izquierdo, text='PELICULAS', font=fuente2, foreground='black', background='beige').pack(side='top')
		self.listbox=Listbox(frame_izquierdo, font=fuente, foreground='NavajoWhite4', width=30, height=15, yscrollcommand=self.barra.set)
		self.barra.config(command=self.listbox.yview)
		
		self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=20)
		self.barra.pack(side=tk.RIGHT, fill=tk.Y)

		self.frame_derecho=Frame()
		self.frame_derecho.pack(side='right')
		self.frame_derecho.configure(bg='beige')
		
		self.manejador=manejador
		self.lista=manejador.getLista()

		for i in range(len(self.lista)):
			text = "{}".format(self.lista[i].getTitulo())
			self.listbox.insert(i,text)

		self.listbox.bind("<Double-Button-1>", self.mostrar)

	def mostrar(self,event):
		seleccion = self.listbox.curselection()

		if seleccion:
			i = seleccion[0]

			lista_generos = self.manejador.Busca_Generos(self.lista[i].getGenero())
			cadena = "  ".join(lista_generos)
			generos = StringVar()
			generos.set(cadena)

			titulo = StringVar()
			fecha = StringVar()
			lenguaje = StringVar()

			fuente=tkFont.Font(family="Bookman Old Style",size= "12",weight="normal")
			fuente2=tkFont.Font(family="Bookman Old Style",size= "12",weight="bold")

			titulo.set(self.lista[i].getTitulo())
			fecha.set('Lanzamiento: '+self.lista[i].getFecha())
			lenguaje.set('Lenguaje: '+self.lista[i].getLenguaje())

			Label(self.frame_derecho,textvariable=titulo,width=31,font=fuente2,justify='center', background='beige').grid(row=1,column=1,padx=20,pady=15)
			Label(self.frame_derecho,textvariable=fecha,font=fuente2,width=20,justify='center', background='beige').grid(row=1,column=0,padx=20,pady=15)
			Label(self.frame_derecho,textvariable=lenguaje,font=fuente2,width=20,justify='center', background='beige').grid(row=1,column=2,padx=20,pady=15)

			resumen=Text(self.frame_derecho,width=80,height=7)
			resumen.grid(row=2,column=0,columnspan=3,pady=20)
			resumen.insert(tk.END,self.lista[i].getResumen())
			resumen.config(state='disabled',font=fuente,foreground='NavajoWhite4')

			Label(self.frame_derecho,textvariable=generos,width=40,justify='center',font=fuente2, background='beige').grid(row=4,column=0,columnspan=3,pady=20)

	def Ejecutar(self):
		self.__ventana.mainloop()
	