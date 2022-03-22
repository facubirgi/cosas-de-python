import pickle
class persona:
	def _init_(self, nombre, genero, edad):
		self.nombre = nombre
		self.genero = genero
		self.edad = edad
		print("Se ha creado una persona nueva con el nombre de ", self.nombre)
	def _str_(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)
class listapersonas:
	personas=[]
	def _init_(self):
		listadepersonas=open("archivoexterno","ab+")
		listadepersonas.seek(0)
		try:
			self.personas=pickle.load(listadepersonas)
			print("Se cargaron {} personas del archivo externo".format(len(self.personas)))
		except:
			print("El archivo esta vacio")
		finally:
			listadepersonas.close()
			del(listadepersonas)
	def agregarpresonas(self, p):
		self.personas.append(p)
		self.guardarpersonasarchivoexterno()
	def mostrarpersonas(self):
		for n in self.personas:
			print(n)
	def guardarpersonasarchivoexterno(self):
		listapersonas=open("archivoexterno", "wb")
		pickle.dump(self.personas, listapersonas)
		listapersonas.close()
		del(listapersonas)
	def mostrarinfoarchivoexterno(self):
		print("La informacion del archivo externo es la siguiente:")
		for x in self.personas:
			print(x)
milista=listapersonas()
perso=persona("monica", "femenino", 34)
milista.agregarpresonas(perso)
milista.mostrarinfoarchivoexterno()