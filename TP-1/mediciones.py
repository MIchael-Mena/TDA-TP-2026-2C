"""Mide el algoritmo greedy y genera los graficos del informe."""

from __future__ import annotations

import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from tp1 import juego_monedas_greedy


# Veinte puntos para reducir el error del ajuste sin exceder el limite practico.
TAMANIOS = list(range(50_000, 1_000_001, 50_000))
REPETICIONES = 3
DIRECTORIO_GRAFICOS = (
    Path(__file__).parent / "informe" / "Informe_TDA_TP_1_2026_2C" / "img"
)


def juego_monedas_solo_puntajes(monedas: list[int]) -> tuple[int, int]:
    """Ejecuta el nucleo greedy sin conservar la secuencia de elecciones."""
    if not monedas:
        raise ValueError("La entrada debe contener al menos una moneda")
    if any(moneda <= 0 for moneda in monedas):
        raise ValueError("Los valores de las monedas deben ser positivos")

    izq = 0
    der = len(monedas) - 1
    puntaje_sophia = 0
    puntaje_mateo = 0
    turno_sophia = True

    while izq <= der:
        if turno_sophia:
            if monedas[izq] >= monedas[der]:
                puntaje_sophia += monedas[izq]
                izq += 1
            else:
                puntaje_sophia += monedas[der]
                der -= 1
        elif monedas[izq] <= monedas[der]:
            puntaje_mateo += monedas[izq]
            izq += 1
        else:
            puntaje_mateo += monedas[der]
            der -= 1
        turno_sophia = not turno_sophia

    return puntaje_sophia, puntaje_mateo


def medir_tiempos(generador, algoritmo) -> list[float]:
    tiempos = []
    for tamanio in TAMANIOS:
        monedas = generador(tamanio)
        mediciones = []
        for _ in range(REPETICIONES):
            inicio = time.perf_counter()
            algoritmo(monedas)
            mediciones.append(time.perf_counter() - inicio)
        tiempos.append(statistics.median(mediciones))
    return tiempos


def ajuste_lineal(x: list[int], y: list[float]) -> tuple[float, float, float]:
    """Calcula a, b y el error cuadratico del ajuste y = a*x + b."""
    cantidad = len(x)
    promedio_x = sum(x) / cantidad
    promedio_y = sum(y) / cantidad
    pendiente = sum(
        (valor_x - promedio_x) * (valor_y - promedio_y)
        for valor_x, valor_y in zip(x, y)
    ) / sum((valor_x - promedio_x) ** 2 for valor_x in x)
    ordenada = promedio_y - pendiente * promedio_x
    error = sum(
        (valor_y - (pendiente * valor_x + ordenada)) ** 2
        for valor_x, valor_y in zip(x, y)
    )
    return pendiente, ordenada, error


def generar_graficos(resultados) -> None:
    DIRECTORIO_GRAFICOS.mkdir(parents=True, exist_ok=True)
    colores = {
        "aleatorio": "tab:blue",
        "creciente": "tab:orange",
        "iguales": "tab:green",
    }
    figura, eje = plt.subplots(figsize=(9, 5))
    ajustes = {}
    for nombre, variantes in resultados.items():
        for variante, tiempos in variantes.items():
            pendiente, ordenada, error = ajuste_lineal(TAMANIOS, tiempos)
            ajustes[(nombre, variante)] = (pendiente, ordenada, error)
            estilo = "-" if variante == "puntajes" else "--"
            eje.plot(
                TAMANIOS,
                tiempos,
                linestyle=estilo,
                marker="o",
                color=colores[nombre],
                label=f"{nombre} ({variante})",
            )
    eje.set_title("Tiempo de ejecucion del algoritmo greedy")
    eje.set_xlabel("Tamano de entrada (n)")
    eje.set_ylabel("Tiempo (segundos)")
    eje.grid(True)
    eje.legend()
    figura.tight_layout()
    figura.savefig(DIRECTORIO_GRAFICOS / "grafico_tiempos.png", dpi=150)
    plt.close(figura)

    figura, eje = plt.subplots(figsize=(9, 5))
    for nombre, variantes in resultados.items():
        for variante, tiempos in variantes.items():
            pendiente, ordenada, _ = ajustes[(nombre, variante)]
            residuos = [
                abs(tiempo - (pendiente * tamanio + ordenada))
                for tamanio, tiempo in zip(TAMANIOS, tiempos)
            ]
            estilo = "-" if variante == "puntajes" else "--"
            eje.plot(
                TAMANIOS,
                residuos,
                linestyle=estilo,
                marker="o",
                color=colores[nombre],
                label=f"{nombre} ({variante})",
            )
    eje.set_title("Error absoluto del ajuste lineal")
    eje.set_xlabel("Tamano de entrada (n)")
    eje.set_ylabel("Error absoluto (segundos)")
    eje.grid(True)
    eje.legend()
    figura.tight_layout()
    figura.savefig(DIRECTORIO_GRAFICOS / "grafico_errores.png", dpi=150)
    plt.close(figura)

    for clave, (pendiente, ordenada, error) in ajustes.items():
        print(
            f"{clave[0]} - {clave[1]}: "
            f"a={pendiente:.3e}, b={ordenada:.3e}, SSE={error:.3e}"
        )


def main() -> None:
    random.seed(12345)
    generadores = {
        "aleatorio": lambda n: [random.randint(1, 1000) for _ in range(n)],
        "creciente": lambda n: list(range(1, n + 1)),
        "iguales": lambda n: [10] * n,
    }
    resultados = {}
    for nombre, generador in generadores.items():
        print(f"Midiendo caso {nombre}...")
        resultados[nombre] = {
            "puntajes": medir_tiempos(generador, juego_monedas_solo_puntajes),
            "completo": medir_tiempos(generador, juego_monedas_greedy),
        }
    generar_graficos(resultados)
    print(f"Graficos generados en {DIRECTORIO_GRAFICOS}")


if __name__ == "__main__":
    main()
