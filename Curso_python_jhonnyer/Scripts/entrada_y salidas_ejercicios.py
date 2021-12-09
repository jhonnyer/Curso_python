#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 09:25:56 2021

@author: root
"""

#Formateo de caracteres y numeros 
print("{:>20}".format("Hola mundo"))
print("{:.3}".format("Hola mundo"))
#Aineamiento al centro en 20 caracteres y truncamiento en el segundo caracter
print("{:^20.1}".format("Hola mundo"))
#formateo a 5 numeros enteros rellenados con cero 
print("{:05d}".format(150))
#formateo a 7 numeros enteros rellenados con espacios
print("{:7d}".format(7887))
#formateo a 3 numeros enteros y 3 numeros decimales. #el numero 7 indica 7 digitos incluyendo el punto
print("{:07.3f}".format(20.02))




