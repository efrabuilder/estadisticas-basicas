"""
main.py
Programa de línea de comandos para calcular media, mediana y moda
de una cantidad de números ingresados por el usuario.
"""

from stats import resumen_estadistico


def leer_datos():
    entrada = input(
        "Ingresá los números separados por espacio o coma (ej: 4 8 15 16 23 8): "
    )
    entrada = entrada.replace(",", " ")
    try:
        datos = [float(x) for x in entrada.split()]
    except ValueError:
        print("Error: asegurate de ingresar solo números.")
        return None

    if not datos:
        print("Error: no ingresaste ningún número.")
        return None

    return datos


def mostrar_resultados(resultado):
    print("\n--- Resultados ---")
    print(f"Media:   {resultado['media']:.4f}")
    print(f"Mediana: {resultado['mediana']:.4f}")

    if resultado["moda"]:
        moda_str = ", ".join(str(m) for m in resultado["moda"])
        print(f"Moda:    {moda_str}")
    else:
        print("Moda:    no hay (todos los valores son únicos)")

    print("\n--- Dispersión ---")
    print(f"Rango:              {resultado['rango']:.4f}")

    if resultado["varianza"] is None:
        print("Varianza:           n/a (se necesitan al menos 2 datos)")
        print("Desv. estándar:     n/a (se necesitan al menos 2 datos)")
    else:
        print(f"Varianza:           {resultado['varianza']:.4f}")
        print(f"Desv. estándar:     {resultado['desviacion_estandar']:.4f}")

    if resultado["coeficiente_variacion"] is None:
        print("Coef. de variación: n/a")
    else:
        print(f"Coef. de variación: {resultado['coeficiente_variacion']:.4f}%")


def main():
    datos = leer_datos()
    if datos is None:
        return
    resultado = resumen_estadistico(datos)
    mostrar_resultados(resultado)


if __name__ == "__main__":
    main()
