#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#formateo numero enteros, rellenar con espacios
#mostar el numero 10, 100 y 1000 cada uno con 4 caracteres
#se rellenen los espacios en blanco con  cero  y que se alinen perfectamente a la derecha
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

print("\n")
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

#formateo con numeros flotantes
print("{:.3f}".format(3.1415926))
#formateo con numeros flotantes, alineado a la derecha 7 espacios
print("Alineado a la derecha 7 espacios y 3 flotantes")
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(152.21))

#formateo con numeros flotantes, alineado a la derecha 7 espacios Y RELLENADO CON CERO
print("Alineado a la derecha 7 espacios, 3 flotantes y rellenado con ceros")
print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(152.21))


#FORMATEO CON FUNCIONALIDAD F DE PYTHON 3.6
nombre="Jhonnyer"
print("FORMATEO CON FUNCION F pasando directamente la variable ")
print(f"Hola {nombre}")

C="{n}-{m}={r}".format(m=2, r=3-2, n=3)
print(C)