#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 09:35:24 2021

@author: root
"""

#Ejercicio 2
#Crea un script llamado tabla.py que realice las siguientes tareas:

#Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
#El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
#En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
#El script contendrá un bucle for que itere el número de veces del primer argumento.
#Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
#Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (**end=''* evita el salto de línea)*.
#Ejecuta el código y observa el resultado.
# Intenta deducir dónde y cómo añadir otra instruccion print() para dibujar una tabla.

import sys
print(sys.argv)
if len(sys.argv)==3:
    filas=int(sys.argv[1])
    columnas=int(sys.argv[2])
    if filas <1 or filas >9 or columnas <1 or columnas >9:
        print("Filas incorrectas, ingresa un número entero del 1 al 9")
        print("Ejemplo Tabla.py [1-9] [1-9]")
    else: 
        # Empieza la logica del script si cumple los parametros 
        for f in range(filas):
            print("")  #permite crear una matriz ya que cada que se ejecuta coloca la salida en la parte de abajo de cada linea
            # print(f)
            for c in range(columnas):
                #End permite que no haya salto de linea en la salida
                print("*", end="") #Resultado 25 * ya que muestra las columnas y filas 5*5=25 veces
                # print(c)
else:
    print("Error, número de argumentos incorrectos")
    print("Ejemplo Tabla.py [1-9] [1-9]")