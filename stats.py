"""
stats.py
Funciones para calcular media, mediana y moda de un conjunto de números.
"""

from collections import Counter


def calcular_media(datos):
    """Devuelve el promedio (media aritmética) de una lista de números."""
    if not datos:
        raise ValueError("La lista de datos no puede estar vacía.")
    return sum(datos) / len(datos)


def calcular_mediana(datos):
    """Devuelve la mediana de una lista de números."""
    if not datos:
        raise ValueError("La lista de datos no puede estar vacía.")

    ordenados = sorted(datos)
    n = len(ordenados)
    mitad = n // 2

    if n % 2 == 0:
        return (ordenados[mitad - 1] + ordenados[mitad]) / 2
    return ordenados[mitad]


def calcular_moda(datos):
    """
    Devuelve la(s) moda(s) de una lista de números.
    Puede haber más de una moda (multimodal). Si todos los valores
    aparecen la misma cantidad de veces, se considera que no hay moda.
    """
    if not datos:
        raise ValueError("La lista de datos no puede estar vacía.")

    conteo = Counter(datos)
    frecuencia_max = max(conteo.values())

    if frecuencia_max == 1:
        return []  # no hay moda: todos los valores son únicos

    modas = [valor for valor, frecuencia in conteo.items() if frecuencia == frecuencia_max]
    return sorted(modas)


def calcular_rango(datos):
    """Devuelve el rango (máximo - mínimo) de una lista de números."""
    if not datos:
        raise ValueError("La lista de datos no puede estar vacía.")
    return max(datos) - min(datos)


def calcular_varianza(datos):
    """
    Devuelve la varianza muestral: s² = Σ(xi - x̄)² / (n - 1).
    Requiere al menos 2 datos.
    """
    n = len(datos)
    if n < 2:
        raise ValueError("Se necesitan al menos 2 datos para calcular la varianza.")
    media = calcular_media(datos)
    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    return suma_cuadrados / (n - 1)


def calcular_desviacion_estandar(datos):
    """Devuelve la desviación estándar muestral: s = √s²."""
    return calcular_varianza(datos) ** 0.5


def calcular_coeficiente_variacion(datos):
    """
    Devuelve el coeficiente de variación como porcentaje: CV = (s / x̄) × 100.
    Requiere que la media sea distinta de cero.
    """
    media = calcular_media(datos)
    if media == 0:
        raise ValueError("No se puede calcular el CV cuando la media es 0.")
    desviacion = calcular_desviacion_estandar(datos)
    return (desviacion / media) * 100


def resumen_estadistico(datos):
    """Devuelve un diccionario con media, mediana, moda y medidas de dispersión."""
    resumen = {
        "media": calcular_media(datos),
        "mediana": calcular_mediana(datos),
        "moda": calcular_moda(datos),
        "rango": calcular_rango(datos),
    }

    if len(datos) >= 2:
        resumen["varianza"] = calcular_varianza(datos)
        resumen["desviacion_estandar"] = calcular_desviacion_estandar(datos)
        try:
            resumen["coeficiente_variacion"] = calcular_coeficiente_variacion(datos)
        except ValueError:
            resumen["coeficiente_variacion"] = None
    else:
        resumen["varianza"] = None
        resumen["desviacion_estandar"] = None
        resumen["coeficiente_variacion"] = None

    return resumen
