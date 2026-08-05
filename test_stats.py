"""
test_stats.py
Pruebas unitarias para las funciones de stats.py
Ejecutar con: python -m unittest test_stats.py
"""

import unittest
from stats import (
    calcular_media,
    calcular_mediana,
    calcular_moda,
    calcular_rango,
    calcular_varianza,
    calcular_desviacion_estandar,
    calcular_coeficiente_variacion,
    resumen_estadistico,
)


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

    def test_rango(self):
        self.assertEqual(calcular_rango([4, 8, 15, 16, 23, 8]), 19)
        self.assertEqual(calcular_rango([5]), 0)

    def test_varianza(self):
        self.assertAlmostEqual(calcular_varianza([2, 4, 6, 8]), 6.6667, places=4)
        with self.assertRaises(ValueError):
            calcular_varianza([5])

    def test_desviacion_estandar(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([2, 4, 6, 8]), 2.5820, places=4)

    def test_coeficiente_variacion(self):
        self.assertAlmostEqual(calcular_coeficiente_variacion([2, 4, 6, 8]), 51.6398, places=4)
        with self.assertRaises(ValueError):
            calcular_coeficiente_variacion([-4, 0, 4])

    def test_resumen_estadistico(self):
        resultado = resumen_estadistico([1, 2, 2, 3, 4])
        self.assertAlmostEqual(resultado["media"], 2.4)
        self.assertEqual(resultado["mediana"], 2)
        self.assertEqual(resultado["moda"], [2])
        self.assertEqual(resultado["rango"], 3)
        self.assertIsNotNone(resultado["varianza"])
        self.assertIsNotNone(resultado["desviacion_estandar"])

    def test_resumen_estadistico_un_solo_dato(self):
        resultado = resumen_estadistico([7])
        self.assertEqual(resultado["rango"], 0)
        self.assertIsNone(resultado["varianza"])
        self.assertIsNone(resultado["desviacion_estandar"])
        self.assertIsNone(resultado["coeficiente_variacion"])


if __name__ == "__main__":
    unittest.main()
