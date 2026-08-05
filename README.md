# Estadísticas Básicas

Programa en Python que calcula la **media**, **mediana** y **moda** de un conjunto de números ingresados por el usuario.

## Estructura del proyecto

```
estadisticas-basicas/
├── main.py         # Programa de línea de comandos
├── stats.py        # Funciones de cálculo (media, mediana, moda)
├── test_stats.py   # Pruebas unitarias
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
```

## Usar las funciones en tu propio código

```python
from stats import calcular_media, calcular_mediana, calcular_moda, resumen_estadistico

datos = [4, 8, 15, 16, 23, 8]

print(calcular_media(datos))     # 12.33
print(calcular_mediana(datos))   # 11.5
print(calcular_moda(datos))      # [8]
print(resumen_estadistico(datos))
```

## Pruebas

```bash
python -m unittest test_stats.py
```

## Notas

- Si todos los valores son distintos, `calcular_moda` devuelve una lista vacía (no hay moda).
- Si hay varios valores con la misma frecuencia máxima, la función devuelve todas las modas (distribución multimodal).

## Licencia

Este proyecto se distribuye bajo la licencia MIT.
