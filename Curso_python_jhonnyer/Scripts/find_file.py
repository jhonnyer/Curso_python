while True:
	narchivo=input("ingrese el nombre del archivo: ")
	try:
		man_a=open(narchivo)
		contador=0
		for linea in man_a:
			linea=linea.rstrip()
			if linea.find("X-DSPAM-Confidence:")==-1:continue
			contador=contador+1	
			print(linea)
		print("El numero de lineas con spam es: ",contador)
		print("El valor medio  de lineas con spam es: ",(contador/2))
		break
	except:
		print("Nombre de archivo '{}' no es valido \n".format(narchivo))
		print("Puedes finalizar el programa con la palabra fin")
		if narchivo=="fin":
			print("Adios")
			break
	
