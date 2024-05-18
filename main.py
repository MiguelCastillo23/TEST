# -*- coding: utf-8 -*-
import sys
sys.path.append('D:\Sem 9.1\src')
from AreaTriangulo import calcular_area_triangulo
5

def main():
    # Solicita los lados del triángulo al usuario
    print("Introduce los tres lados del triángulo:")
    a = float(input("Lado a: "))
    b = float(input("Lado b: "))
    c = float(input("Lado c: "))

    # Calcula y muestra el área del triángulo
    area = calcular_area_triangulo(a, b, c)
    print("El área del triángulo con lados {}, {} y {} es: {:.2f}".format(a, b, c, area))


if __name__ == "__main__":
    main()
