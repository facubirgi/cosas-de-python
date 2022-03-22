from tkinter import *
from tkinter import messagebox

raiz=Tk()

def infoAdicional():
	messagebox.showinfo("Procesador de texto", "Version 2020 Python 3.x")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Licencia Trial")

def salirAplicacion():
	valor=messagebox.askquestion("Salir", "¿Deseas salir de al aplicación?")
	if valor =="yes":
		raiz.destroy()
def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
	if valor == False:
		raiz.destroy()


barraMenu=Menu(raiz)

raiz.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

EdicionMenu=Menu(barraMenu, tearoff=0)
EdicionMenu.add_command(label="Copiar")
EdicionMenu.add_command(label="Cortar")
EdicionMenu.add_command(label="Pegar")
EdicionMenu.add_separator()
EdicionMenu.add_command(label="Deshacer")
EdicionMenu.add_command(label="Rehacer")

HerramientaMenu=Menu(barraMenu, tearoff=0)
HerramientaMenu.add_command(label="Ajuste de linea")
HerramientaMenu.add_command(label="Fuente")

AyudaMenu=Menu(barraMenu, tearoff=0)
AyudaMenu.add_command(label="Licencia", command=avisoLicencia)
AyudaMenu.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=EdicionMenu)
barraMenu.add_cascade(label="Herramientas", menu=HerramientaMenu)
barraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)

raiz.mainloop()