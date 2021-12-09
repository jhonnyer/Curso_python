#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 12:54:00 2021

@author: root
"""

class Pelicula:
    #Constructor de clase
    def __init__(self,titulo, duracion, lanzamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.lanzamiento=lanzamiento
        print("Se ha creado la pelicula '{}'".format(titulo))
    
    #Destructor de clase
    def __del__(self):
#         print("Se esta borrando la pelicula '",self.titulo,"' de la memoria")
        print("Se esta borrando la pelicula '{}' de la memoria".format(self.titulo))

p=Pelicula("El padrino",175, 1972)
#del(p)