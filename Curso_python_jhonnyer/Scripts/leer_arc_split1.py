manejador = open('mbox.txt')
contador=0
for linea in manejador:
	palabras = linea.split()
	# print 'Depuración:', palabras
	if len(palabras) == 0 or palabras[0] != 'From' : continue
	print(palabras)
