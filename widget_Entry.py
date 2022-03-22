from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar()

cuadroTexto=Entry(miFrame, textvariable=minombre)
cuadroTexto.grid(row=0,column=1, padx=5, pady=5)
cuadroTexto.config(fg="Red", justify="center")

cuadroTexto2=Entry(miFrame)
cuadroTexto2.grid(row=1,column=1, padx=5, pady=5)
cuadroTexto2.config(show="*")

cuadroTexto3=Entry(miFrame)
cuadroTexto3.grid(row=2,column=1, padx=5, pady=5)


textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=5, pady=5)

scrollVertical=Scrollbar(miFrame, command=textoComentario.yview)
scrollVertical.grid(row=4, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVertical.set)

nombreLabel=Label(miFrame, text="Usuario:")
nombreLabel.grid(row=0,column=0, sticky="w", padx=5, pady=5)

nombreLabel2=Label(miFrame, text="Contraseña:")
nombreLabel2.grid(row=1,column=0, sticky="w", padx=5, pady=5)

nombreLabel3=Label(miFrame, text="Direccion:")
nombreLabel3.grid(row=2,column=0,sticky="w", padx=5, pady=5)

nombreLabel4=Label(miFrame, text="Comentarios:")
nombreLabel4.grid(row=4,column=0,sticky="w", padx=5, pady=5)

def codigoBoton():

	minombre.set("Facundo")

miBotonenvio=Button(raiz, text="Mostrar Contraseña", command=codigoBoton)

miBotonenvio.pack()

raiz.mainloop()