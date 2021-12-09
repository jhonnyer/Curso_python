#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:00:13 2021

@author: root
"""

# Ejercicio 3
# Crea un script llamado descomposicion.py que realice las siguientes tareas:

# Debe tomar 1 argumento que será un número entero positivo.
# En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
# El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3647:


# python descomposicion.py 3647
# El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:


import sys
if len(sys.argv)==2:
        numero=int(sys.argv[1])
        if numero<0 or numero  >9999:
            print("Error, el número ingresado es incorrecto")
            print("Ejemplo, descomposicion.py [0-9999]")
        else:
            # Logica del ejercicio 
            cadena=str(numero) #se convierte en cadena para poder ver la longitud de la variable numero
            longitud=len(cadena)
            for i in range(longitud):
                #ordena la salida en el ultimo digito al primero, ejemplo: entrada 1234, salida: 4321. NOTA: ** es equivalente a elevado potencia  ^
                print("{:04d}".format(int(cadena[longitud-1-i])*10**i)) #ejemplo posicionamiento; primer iteracion (4-1-0)*10⁰=3; segunda iteracion (4-1-1)*10¹=20; tercera iteracion (4-1-2)*10²=100; cuarta iteracion: (4-1-3)*10³=0000 
    
else:
    print("Error, argumentos invalidos")
    print("Ejemplo descomposicion.py [0-9999]")