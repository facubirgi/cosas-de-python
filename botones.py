from tkinter import *
raiz=Tk()
varOpcion=IntVar()
def imprimir():
	#print(varOpcion.get())
	if varOpcion.get()==1:
		etiqueta.config(text="Has elegido Masculino")
	elif varOpcion.get()==2:
		etiqueta.config(text="Has elegido Femenino")
	else:
		etiqueta.config(text="Has elegido Otros / Otras")
Label(raiz, text="Genero:").pack()
Radiobutton(raiz, text="Masculino", variable=varOpcion,value=1, command=imprimir).pack()
Radiobutton(raiz, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()
Radiobutton(raiz, text="Otros/Otras", variable=varOpcion, value=3, command=imprimir).pack()
etiqueta=Label(raiz)
etiqueta.pack()
raiz.mainloop()