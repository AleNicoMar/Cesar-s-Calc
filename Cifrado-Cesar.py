# -*- coding: utf-8 -*-

# Importo el módulo 'os' que, en este caso, contiene funciones del SO tales como 'cls' o 'pause>nul'
import os

# Declaro los abecedarios a utilizar.
alf = "abcdefghijklmnñopqrstuvwxyz"
alf2 = alf.upper() # Este está en mayúsculas.

def main():
	loop = True
	while (loop == True):
		opcion = input("¿Qué es lo que quiere hacer?\n > ")
		if (opcion == "cifrar" or opcion == "c"):
			os.system('cls')
			plano = input("Inserte el texto plano:\n > ").lower()
			llave = input("Inserte el desplazamiento:\n > ")
			os.system('cls')
			f = open('MensajeCif.txt', 'w')		# Abro el archivo "MensajeCif.txt"(si no existe se crea) en modo escritura y lo guardo en la variable 'f'.
			f.write(cifrar(plano, llave))		# Escribo el resultado de la función cifrar en el archivo "MensajeCif.txt".
			print("El mensaje ha sido cifrado satisfactoriamente.")
			os.system('pause>nul')

		elif (opcion == "decifrar" or opcion == "d"):
			os.system('cls')
			key = input("Inserte el desplazamiento:\n > ")
			os.system('cls')
			l = open('MensajeCif.txt', 'r')		# Abro el archivo "MensajeCif.txt"(si no existe, tira error) en modo lectura y lo guardo en la variable 'l'.
			f = open('MensajeDec.txt', 'w')		# Abro el archivo "MensajeDec.txt"(si no existe, tira error) en modo lectura y lo guardo en la variable 'f'.
			f.write(decifrar(l.read(), key))	# Escribo el resultado de la función decifrar en el archivo "MensajeDec.txt".
			print("El mensaje ha sido decifrado satisfactoriamente.")
			os.system('pause>nul')

		elif (opcion == "salir" or opcion == "s"):
			loop = False

		else:
			print("Ingrese un valor correcto.")

# La función cifrar realiza la operación: { Cifrado = (x + n) % 28 } <- En Wikipedia está bien explicada la fórmula.
def cifrar(texto, llave):
	cifrado = ""
	for letra in texto:
		suma = alf.find(letra) + int(llave)
		modulo = int(suma) % len(alf)
		cifrado = cifrado + str(alf[modulo])
		print(cifrado)
		os.system('sleep(1000)')
		os.system('cls')
	return cifrado.upper() # Devuelve todo en mayúsculas.

# La función cifrar realiza la operación inversa que también está en Wikipedia.
def decifrar(texto, llave):
	cifrado = ""
	for letra in texto:
		resta = alf2.find(letra) - int(llave)
		modulo = int(resta) % len(alf2)
		cifrado = cifrado + str(alf2[modulo])
		print(cifrado)
		os.system('sleep(1000)')
		os.system('cls')
	return cifrado.upper()

# Llamo a la función main, es decir, da inicio al programa
main()