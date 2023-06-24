from tkinter import *
from tkinter import ttk, messagebox
class Aplicacion():
	__ventana:None
	__total:None
	def __init__(self):
		self.__ventana=Tk()
		self.__ventana.title('Calculadora IPC')
		self.__ventana.configure(bg='SkyBlue1')
		self.__total=StringVar()


		self.mainframe = Frame()
		self.mainframe.pack()
		self.mainframe.configure(bg='SkyBlue1')
		ttk.Label(self.mainframe, text="Item", background='SkyBlue1').grid(column=0, row=0, padx=10, pady=10)
		ttk.Label(self.mainframe, text="Cantidad",background='SkyBlue1').grid(column=1, row=0, padx=10, pady=10)
		ttk.Label(self.mainframe, text="Precio Año Base",background='SkyBlue1').grid(column=2, row=0, padx=10, pady=10)
		ttk.Label(self.mainframe, text="Precio Año Actual", background='SkyBlue1').grid(column=3, row=0, padx=10, pady=10)
		ttk.Label(self.mainframe, text="Vestimenta", background='SkyBlue1').grid(column=0, row=1, padx=10, pady=10)
		ttk.Label(self.mainframe, text="Alimentos", background='SkyBlue1').grid(column=0, row=2, padx=10, pady=10)
		ttk.Label(self.mainframe, text="Educacion", background='SkyBlue1').grid(column=0, row=3, padx=10, pady=10)


		self.cantVest = Entry(self.mainframe, bg='beige')
		self.cantVest.grid(padx=10, pady=10, row=1, column=1)

		self.precioBVest = Entry(self.mainframe, bg='beige')
		self.precioBVest.grid(padx=10, pady=10, row=1, column=2)

		self.precioAVest = Entry(self.mainframe, bg='beige')
		self.precioAVest.grid(padx=10, pady=10, row=1, column=3)

		self.cantAlim=Entry(self.mainframe,bg='beige')
		self.cantAlim.grid(padx=10, pady=10, row=2, column=1)

		self.precioBAlim=Entry(self.mainframe, bg='beige')
		self.precioBAlim.grid(padx=10, pady=10, row=2, column=2)

		self.precioAAlim=Entry(self.mainframe, bg='beige')
		self.precioAAlim.grid(padx=10, pady=10, row=2, column=3)

		self.cantEdu=Entry(self.mainframe, bg='beige')
		self.cantEdu.grid(padx=10, pady=10, row=3, column=1)

		self.precioBEdu=Entry(self.mainframe, bg='beige')
		self.precioBEdu.grid(padx=10, pady=10, row=3, column=2)

		self.precioAEdu=Entry(self.mainframe, bg='beige')
		self.precioAEdu.grid(padx=10, pady=10, row=3, column=3)

		Button(self.mainframe, text="Calcular IPC", command=self.calcular, background='beige').grid(column=1, row=5, pady=10, padx=10)
		Button(self.mainframe, text='Salir', command=self.__ventana.destroy, background='beige', width=10).grid(column=2, row=5, pady=10, padx=10)
		ttk.Label(self.mainframe, text='IPC %', background='SkyBlue1').grid(column=0, row=6, padx=10, pady=10)
		
		self.__ventana.mainloop()
	def calcular(self):
		try:
			costoBase=float((int(self.cantVest.get())*int(self.precioBVest.get()))+(int(self.cantEdu.get())*int(self.precioBEdu.get()))+(int(self.cantAlim.get())*int(self.precioBAlim.get())))
			costoActual=float((int(self.cantVest.get())*int(self.precioAVest.get()))+(int(self.cantEdu.get())*int(self.precioAEdu.get()))+(int(self.cantAlim.get())*int(self.precioAAlim.get())))
			self.__total=int((costoActual/costoBase)*100)
			self.__total=str(self.__total)+'%'
			ttk.Label(self.mainframe, text=self.__total, background='beige').grid(column=1, row=6, padx=10, sticky=W )
			
			
		except ValueError:
			messagebox.showerror(title='Error', message='Debe ingresar un valor en todas las casillas')
if __name__ == '__main__':
	ventana=Aplicacion()