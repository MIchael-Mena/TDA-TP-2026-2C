"""Casos pendientes para el algoritmo greedy del TP1."""

import unittest

from tp1 import leer_monedas, resolver


class TestLeerMonedas(unittest.TestCase):
    def test_lee_valores_separados_por_espacios(self):
        # TODO: completar con un archivo temporal cuando se cierre el formato.
        self.skipTest("TODO: fijar y probar el formato definitivo de entrada")


@unittest.skip("TODO: implementar el algoritmo greedy")
class TestResolver(unittest.TestCase):
    def test_una_moneda(self):
        self.assertIsNotNone(resolver([7]))

    def test_dos_monedas(self):
        self.assertIsNotNone(resolver([2, 9]))

    def test_cantidad_impar(self):
        self.assertIsNotNone(resolver([1, 5, 2, 10, 6]))

    def test_cantidad_par(self):
        self.assertIsNotNone(resolver([4, 1, 8, 3]))

    def test_empates(self):
        self.assertIsNotNone(resolver([5, 5, 2, 5]))

    def test_resultado_optimo_contra_referencia(self):
        # TODO: comparar contra una solución exhaustiva para entradas pequeñas.
        self.assertIsNotNone(resolver([3, 8, 2, 7]))


if __name__ == "__main__":
    unittest.main()
