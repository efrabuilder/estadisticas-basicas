# Estadísticas Básicas

Programa en Python que calcula un **resumen de datos** (cuenta, suma, mínimo, máximo), la **media**, **mediana**, **moda**, las principales **medidas de dispersión** (rango, varianza, desviación estándar, error típico y coeficiente de variación) y las **medidas de forma** (coeficiente de asimetría y curtosis) de un conjunto de números ingresados por el usuario. Las fórmulas de asimetría y curtosis coinciden con `SESGO`/`SKEW` y `CURTOSIS`/`KURT` de Excel.

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

--- Resumen de datos ---
Cuenta:  6
Suma:    74.0000
Mínimo:  4.0000
Máximo:  23.0000

--- Resultados ---
Media:   12.3333
Mediana: 11.5000
Moda:    8

--- Dispersión ---
Rango:              19.0000
Varianza:           48.2667
Desv. estándar:     6.9474
Error típico:       2.8363
Coef. de variación: 56.3304%

--- Medidas de forma ---
Coef. de asimetría: 0.4835
Curtosis:           -0.6298
```

## Usar las funciones en tu propio código

```python
from stats import (
    calcular_media,
    calcular_mediana,
    calcular_moda,
    calcular_rango,
    calcular_cuenta,
    calcular_suma,
    calcular_minimo,
    calcular_maximo,
    calcular_varianza,
    calcular_desviacion_estandar,
    calcular_coeficiente_variacion,
    calcular_error_tipico,
    calcular_asimetria,
    calcular_curtosis,
    resumen_estadistico,
)

datos = [4, 8, 15, 16, 23, 8]

print(calcular_cuenta(datos))                  # 6
print(calcular_suma(datos))                    # 74
print(calcular_minimo(datos))                  # 4
print(calcular_maximo(datos))                  # 23
print(calcular_media(datos))                   # 12.33
print(calcular_mediana(datos))                 # 11.5
print(calcular_moda(datos))                    # [8]
print(calcular_rango(datos))                   # 19
print(calcular_varianza(datos))                # 48.2667 (muestral, n - 1)
print(calcular_desviacion_estandar(datos))      # 6.9474
print(calcular_error_tipico(datos))            # 2.8363
print(calcular_coeficiente_variacion(datos))    # 56.3304
print(calcular_asimetria(datos))               # 0.4835 (igual que SESGO/SKEW en Excel)
print(calcular_curtosis(datos))                # -0.6298 (igual que CURTOSIS/KURT en Excel)
print(resumen_estadistico(datos))
```

## Pruebas

```bash
python -m unittest test_stats.py
```

## Notas

- Si todos los valores son distintos, `calcular_moda` devuelve una lista vacía (no hay moda).
- Si hay varios valores con la misma frecuencia máxima, la función devuelve todas las modas (distribución multimodal).
- La varianza, la desviación estándar y el error típico son **muestrales** (dividen entre `n - 1`) y requieren al menos 2 datos.
- El coeficiente de variación no está definido cuando la media es 0.
- El coeficiente de asimetría requiere al menos 3 datos; la curtosis requiere al menos 4.
- Asimetría y curtosis usan las mismas fórmulas que Excel (`SESGO`/`SKEW` y `CURTOSIS`/`KURT`), por lo que los resultados van a coincidir con una hoja de cálculo.

## Licencia

Este proyecto se distribuye bajo la licencia MIT.
