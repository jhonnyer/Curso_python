narchivo=input("ingrese el nombre del archivo: ")
try:
	man_a=open(narchivo)
except:
	print("nombre archivo {} no existe".format(narchivo))
	exit()
for linea in man_a:
	linea=linea.upper()
	if not linea.startswith('FROM:'):continue
	print(linea)
