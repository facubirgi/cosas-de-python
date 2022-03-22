from tkinter import *

raiz=Tk()

barraMenu=Menu(raiz)

raiz.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

EdicionMenu=Menu(barraMenu, tearoff=0)
EdicionMenu.add_command(label="Cortar")
EdicionMenu.add_command(label="Copiar")
EdicionMenu.add_command(label="Pegar")
EdicionMenu.add_command(label="Deshacer")
EdicionMenu.add_command(label="Rehacer")

HerramientaMenu=Menu(barraMenu, tearoff=0)
HerramientaMenu.add_command(label="Ajuste de linea")
HerramientaMenu.add_command(label="Fuente")

AyudaMenu=Menu(barraMenu, tearoff=0)
AyudaMenu.add_command(label="Licencia")
AyudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=EdicionMenu)
barraMenu.add_cascade(label="Herramientas", menu=HerramientaMenu)
barraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)

raiz.mainloop()