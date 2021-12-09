manejador_archivo = open('mbox.txt')
inp = manejador_archivo.read()
#Ver cuantos caracteres tiene el archivo
print(len(inp))
#imprimir una cadena  hasta la posicion :20
print(inp[:20])


man_a = open('mbox.txt')
contador = 0
for linea in man_a:
	if linea.startswith('From:'):
		print(linea)
