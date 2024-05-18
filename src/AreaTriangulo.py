# -*- coding: utf-8 -*-

import math

def calcular_area_triangulo(a, b, c):
    # Verifica si los lados forman un triángulo válido
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("Los lados no forman un triángulo válido")

    # Calcula el semiperímetro
    s = (a + b + c) / 2

    # Calcula el área usando la fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
