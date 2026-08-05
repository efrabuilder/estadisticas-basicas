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


def resumen_estadistico(datos):
    """Devuelve un diccionario con media, mediana y moda."""
    return {
        "media": calcular_media(datos),
        "mediana": calcular_mediana(datos),
        "moda": calcular_moda(datos),
    }
