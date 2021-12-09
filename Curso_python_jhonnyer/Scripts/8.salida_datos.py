#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 23:51:17 2021

@author: root
"""

texto="otro texto"
n=10

print("Texto sin  formateo")
print("Texto ",texto," y numero ",n)
print("\nTexto con  formateo")
print("Texto {} y un número {}".format(texto,n))

print("\nTexto con formateo cambiando posicion de los elementos")
print("Texto {1} y un número {0}".format(texto,n))

print("\nTexto con formateo referenciando cada variable con un código. No importa el orden")
print("Texto {texto} y un número {numero}".format(numero=n, texto=texto))

print("\nTexto con formateo TEXTO")
print("Texto {t}, {t}, {t}".format(t=texto))

print("\nTexto alineado a la derecha con 30 caracteres de espacio")
print("Texto {:>30} ".format("HOLA MUNDO"))

print("\nTexto alineado a la izquierda con 30 caracteres de espacio")
print("Texto {:30} ".format("HOLA MUNDO"))

print("\nTexto alineado hacia el centro con 30 caracteres de espacio")
print("Texto {:^30} ".format("HOLA MUNDO"))


print("\nTexto alineado en el centro")
print("Texto {T:>30} ".format(T=texto, N=n))

print("\nTRUNCAMIENTO variable 'otro texto', los 4 primeros caracteres")
print("{T:.4} ".format(T=texto, N=n))

print("\nTRUNCAMIENTO 4 caracteres y ALINEACION AL CENTRO 50 CARACTERES")
print("{T:^50.4} ".format(T=texto, N=n))