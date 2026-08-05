"""
test_stats.py
Pruebas unitarias para las funciones de stats.py
Ejecutar con: python -m unittest test_stats.py
"""

import unittest
from stats import calcular_media, calcular_mediana, calcular_moda, resumen_estadistico


class TestEstadisticas(unittest.TestCase):

    def test_media(self):
        self.assertEqual(calcular_media([1, 2, 3, 4, 5]), 3)
        self.assertAlmostEqual(calcular_media([2, 4, 6]), 4.0)

    def test_mediana_impar(self):
        self.assertEqual(calcular_mediana([7, 1, 3]), 3)

    def test_mediana_par(self):
        self.assertEqual(calcular_mediana([1, 2, 3, 4]), 2.5)

    def test_moda_simple(self):
        self.assertEqual(calcular_moda([1, 2, 2, 3]), [2])

    def test_moda_multimodal(self):
        self.assertEqual(calcular_moda([1, 1, 2, 2, 3]), [1, 2])

    def test_moda_sin_repeticion(self):
        self.assertEqual(calcular_moda([1, 2, 3]), [])

    def test_lista_vacia_lanza_error(self):
        with self.assertRaises(ValueError):
            calcular_media([])
        with self.assertRaises(ValueError):
            calcular_mediana([])
        with self.assertRaises(ValueError):
            calcular_moda([])

    def test_resumen_estadistico(self):
        resultado = resumen_estadistico([1, 2, 2, 3, 4])
        self.assertAlmostEqual(resultado["media"], 2.4)
        self.assertEqual(resultado["mediana"], 2)
        self.assertEqual(resultado["moda"], [2])


if __name__ == "__main__":
    unittest.main()
