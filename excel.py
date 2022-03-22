import pandas
import requests
import statistics 
r= requests.get("https://api.recursospython.com/dollar")
cotizacion= statistics.mean(r.json().values())
print(cotizacion)
def dolar_a_pesos(precio_en_usd): # le damos los parámetros que tenemos en Excel
	return precio_en_usd * cotizacion # retorna el valor convertido 

excel=pandas.read_excel("practicas")
excel["precio peso"]=excel["precio dólar"].apply(dolar_a_pesos)
excel.to_excel("ProductosPesificados.xlsx", index=False)
