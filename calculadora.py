import os
import sys
import time

def suma():
	A = raw_input("ingrese valor de A: ")
	B = raw_input("ingrese valor de B: ")
	#condicion si encuentran letras.
	if A.isalpha() == True or B.isalpha() == True:
		print "no premitido"
		os.system ("cls")
		suma()
	else:
		print int(A)+int(B)
		time.sleep(2)
		os.system ("cls")
		menu()

def resta():
	A = raw_input("ingrese valor de A: ")
	B = raw_input("ingrese valor de B: ")
	#condicion si encuentran letras.
	if A.isalpha() == True or B.isalpha() == True:
		print "no premitido"
		os.system ("cls")
		resta()
	else:
		print int(A)-int(B)
		time.sleep(2)
		os.system ("cls")
		menu()

def multiplicacion():
	A = raw_input("ingrese valor de A: ")
	B = raw_input("ingrese valor de B: ")
	if A.isalpha() == True or B.isalpha() == True:
		print "no premitido"
		os.system ("cls")
		multiplicacion()
	else:
		print int(A)*int(B)
		time.sleep(2)
		os.system ("cls")
		menu()

def dividir():
	A = raw_input("ingrese valor de A: ")
	B = raw_input("ingrese valor de B: ")
	if A.isalpha() == True or B.isalpha() == True:
		print "no premitido"
		os.system ("cls")
		multiplicacion()
	else:
		print int(A)/int(B)
		time.sleep(2)
		os.system ("cls")
		menu()


def menu():
	print "           "
	print "           "
	print "           "
	print "                                      >>>>>CALCULADORA<<<<<<"
	print "                                           -----------"
	print "                        "
	print "     1 suma."
	print "           "
	print "     2 resta."
	print "            "
	print "     3 multiplicacion."
	print "            "
	print "     4 dividir."
	print "            "

	Numero = raw_input("ingrese el numero: ")

	if Numero.isalpha() == True:
		print "            "
		print "               NO SE PERMITEN LETRAS"
		time.sleep(1)
		os.system("cls")
		menu()


	else:
		if Numero =="1":
			print "                     PUEDE EMPESARA A SUMA"
			suma()
		elif Numero =="2":
			print "                     PUEDE EMPESAR A RESTAR"
			resta()
		elif Numero =="3":
			print "                     PUEDE EMPESAR A MULTIPLICAR"
			multiplicacion()
		elif Numero =="4":
			print "                     PUEDE EMPESAR A DIVIDIR"
			dividir()
		else:
			print "Numero Erroneo"
			time.sleep(1)
			os.system("cls")
			menu()
menu()

