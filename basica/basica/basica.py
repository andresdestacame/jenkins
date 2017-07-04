# -*- coding: utf-8 -*-
# 123ABCCDEqq12345678
import Levenshtein
import fuzzy

def basica(numero):
    suma = 0
    for x in range(0, numero):
        suma += x
    return suma

valor = basica(5)

print(valor)
