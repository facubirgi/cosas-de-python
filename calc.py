raiz =Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

operacion=""   
resultado=0

numeroPantalla=StringVar()
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")
#---------------------Pulsaciones teclado
def numeroPulsado(num):
	global operacion
	if operacion != "":
		numeroPantalla.set(num)
		operacion = ""
	else:
		numeroPantalla.set(numeroPantalla.get() + num)


#--------------------Funcion suma
def suma(num):
	global operacion
	global resultado
	resultado += int (num) 
	operacion="suma"
	numeroPantalla.set(resultado)
	#---------------el_resultado
def el_resultado():
	global resultado
	numeroPantalla.set(resultado+int(numeroPantalla.get()))
	resultado=0



#---------------Fila1---------------
boton7=Button(miFrame, text="7", width=13, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=13, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=13, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width=13)
botonDiv.grid(row=2, column=4)
#---------------Fila2---------------
Boton4=Button(miFrame, text="4", width=13, command=lambda:numeroPulsado("4"))
Boton4.grid(row=3, column=1)
Boton5=Button(miFrame, text="5", width=13, command=lambda:numeroPulsado("5"))
Boton5.grid(row=3, column=2)
Boton6=Button(miFrame, text="6", width=13, command=lambda:numeroPulsado("6"))
Boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="X", width=13)
botonMult.grid(row=3, column=4)

#---------------Fila3---------------
boton1=Button(miFrame, text="1", width=13, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=13, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=13, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonMen=Button(miFrame, text="-", width=13)
botonMen.grid(row=4, column=4)

#---------------Fila4---------------
Boton0=Button(miFrame, text="0", width=13, command=lambda:numeroPulsado("0"))
Boton0.grid(row=5, column=1)
BotonComa=Button(miFrame, text=",", width=13, command=lambda:numeroPulsado(","))
BotonComa.grid(row=5, column=2)
BotonIgual=Button(miFrame, text="=", width=13, command=lambda:(el_resultado()))
BotonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=13, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)

raiz.mainloop()