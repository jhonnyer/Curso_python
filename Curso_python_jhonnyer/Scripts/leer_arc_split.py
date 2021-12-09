narchivo = input('Ingresa un nombre de archivo: ')
try:
	man_a = open(narchivo)
except:
	print('No se puede abrir el archivo:', narchivo)
	exit()

for linea in man_a:
	linea=linea.rstrip()
	if not linea.startswith('From '):continue
	palabras=linea.split()
	print(palabras)
