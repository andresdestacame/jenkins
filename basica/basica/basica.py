# -*- coding: utf-8 -*-

# Cambio 1
# Cambio 2

###################
## Archivo - Dev ##
###################

import Levenshtein
import fuzzy

def basica(numero):
    suma = 0
    for x in range(0, numero):
        suma += x
    return suma

valor = basica(5)

########################
## Lineas adicionales ##
########################

print(valor)
