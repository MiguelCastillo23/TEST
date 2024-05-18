# -*- coding: utf-8 -*-
import unittest
import sys

# Agrega la ruta al directorio src al sys.path
sys.path.append('D:\Sem 9.1\src')

# Importa el módulo del que deseas hacer las pruebas
from AreaTriangulo import calcular_area_triangulo

class TestAreaTriangulo(unittest.TestCase):
    def test_calculo_area_triangulo(self):
        # Casos de prueba y resultados esperados
        casos_de_prueba = [
            ((3, 4, 5), 6.00),
            ((12, 11, 14), 63.71),
            ((7, 8, 10), 27.81),
            ((9, 12, 15), 54.00),
            ((8, 15, 17), 60.00),
            ((5, 12, 13), 30.00),
            ((10, 24, 26), 120.00),
            ((6, 7, 8), 20.33),
            ((15, 20, 25), 150.00),
            ((7.5, 9, 12.5), 33.75)
        ]

        # Comprueba el resultado para cada caso de prueba
        for entrada, resultado_esperado in casos_de_prueba:
            resultado = calcular_area_triangulo(*entrada)
            self.assertAlmostEqual(resultado, resultado_esperado, delta=0.01)


if __name__ == '__main__':
    unittest.main()