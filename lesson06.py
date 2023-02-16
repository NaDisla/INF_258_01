# LIBRERIAS / MÓDULOS:
import math # Llamar librería completa
from math import sqrt, sin, cos, tan # Llamar elementos por separado
import random as my_rand # Colocar alias a librería
import figuras # Librería externa (dentro de su carpeta)

raiz = sqrt(81)
new_number = my_rand.randint(500, 900)
print(new_number)

area_circulo = figuras.circulo(4)
area_cuadrado = figuras.cuadrado(6)
area_triangulo = figuras.triangulo(10, 5)

print(area_circulo, area_cuadrado, area_triangulo)
