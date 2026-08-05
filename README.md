# Estadísticas Básicas

Programa en Python que calcula la **media**, **mediana**, **moda** y las principales **medidas de dispersión** (rango, varianza, desviación estándar y coeficiente de variación) de un conjunto de números ingresados por el usuario.

## Estructura del proyecto

```
estadisticas-basicas/
├── main.py         # Programa de línea de comandos
├── stats.py        # Funciones de cálculo (tendencia central y dispersión)
├── test_stats.py   # Pruebas unitarias
├── index.html      # Demo interactiva en el navegador
└── README.md
```

## Requisitos

- Python 3.8 o superior (no requiere librerías externas)

## Uso

```bash
python main.py
```

El programa va a pedir que ingreses una serie de números separados por espacio o coma:

```
Ingresá los números separados por espacio o coma (ej: 4 8 15 16 23 8): 4 8 15 16 23 8

--- Resultados ---
Media:   12.3333
Mediana: 11.5000
Moda:    8

--- Dispersión ---
Rango:              19.0000
Varianza:           48.2667
Desv. estándar:     6.9474
Coef. de variación: 56.3304%
```

## Usar las funciones en tu propio código

```python
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

datos = [4, 8, 15, 16, 23, 8]

print(calcular_media(datos))                   # 12.33
print(calcular_mediana(datos))                 # 11.5
print(calcular_moda(datos))                    # [8]
print(calcular_rango(datos))                   # 19
print(calcular_varianza(datos))                # 48.2667 (muestral, n - 1)
print(calcular_desviacion_estandar(datos))      # 6.9474
print(calcular_coeficiente_variacion(datos))    # 56.3304
print(resumen_estadistico(datos))
```

## Pruebas

```bash
python -m unittest test_stats.py
```

## Notas

- Si todos los valores son distintos, `calcular_moda` devuelve una lista vacía (no hay moda).
- Si hay varios valores con la misma frecuencia máxima, la función devuelve todas las modas (distribución multimodal).
- La varianza y la desviación estándar son **muestrales** (dividen entre `n - 1`) y requieren al menos 2 datos.
- El coeficiente de variación no está definido cuando la media es 0.

## Licencia

Este proyecto se distribuye bajo la licencia MIT.
