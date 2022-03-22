import sqlite3
miconexion=sqlite3.connect("mybase")
mipuntero=miconexion.cursor()

#mipuntero.execute("CREATE TABLE PRODUCTOS (NOMBRE_ART VARCHAR (50), PRECIO INTEGER, SECCION VARCHAR(20)) ")
#mipuntero.execute("INSERT INTO PRODUCTOS VALUES ('PELOTA', 150 , 'DEPORTES')")
variospruductos=[
	("CAMISETA", 900, "DEPORTES"),
	("BOTINES", 4500, "DEPORTES"),
	("BOLSO", 900, "ACCESORIOS"),
	("MALLA", 1200,"ARENA")
]
mipuntero.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variospruductos)
miconexion.commit()

miconexion.close()