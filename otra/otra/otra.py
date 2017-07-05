# -*- coding: utf-8 -*-
# Comentario Andres Martinez...
import Levenshtein
import fuzzy

def otra(numero):
    suma = 0
    for x in range(0, numero):
        suma += x
    return suma

valor = otra(5)

print(valor)
