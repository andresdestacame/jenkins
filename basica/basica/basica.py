# -*- coding: utf-8 -*-

# Modificado desde colaborador Destacame

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
