#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#cODIFO QUE PERMITE ENVIAR DOS ARGUMENTOS, 
#PRIMER ARGUMENTO UN TEXTO. SEGUNDO ARGUMENTO NUMERO DE VECES QUE SE VA A REPETIR EN UN FOR 
import sys
#pasamos el primero argumento, ya que el elemento 0 es el nombre del script
texto=sys.argv[1] 
repeticiones=int(sys.argv[2]) #convertimos en entero ya que los argumentos se envian como caracteres
for x in range(repeticiones):
    print(texto)

