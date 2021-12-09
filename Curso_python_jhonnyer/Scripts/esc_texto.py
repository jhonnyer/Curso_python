fsal = open('salida.txt', 'w')
print(fsal)
linea1 = "Aquí está el zarzo,\n"
fsal.write(linea1)
linea2 = 'el símbolo de nuestra tierra.\n'
fsal.write(linea2)
fsal.close()
