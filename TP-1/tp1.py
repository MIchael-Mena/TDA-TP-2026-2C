"""Interfaz provisional del TP1 de monedas."""

from __future__ import annotations

import sys
from pathlib import Path
import re


def leer_monedas(ruta: str | Path) -> list[int]:
    """Lee valores enteros positivos separados por espacios o punto y coma."""
    contenido = Path(ruta).read_text(encoding="utf-8")
    contenido = "\n".join(linea.split("#", 1)[0] for linea in contenido.splitlines())
    try:
        monedas = [int(valor) for valor in re.split(r"[;\s]+", contenido) if valor]
    except ValueError as error:
        raise ValueError("La entrada debe contener únicamente enteros") from error

    if not monedas:
        raise ValueError("La entrada debe contener al menos una moneda")
    if any(moneda <= 0 for moneda in monedas):
        raise ValueError("Los valores de las monedas deben ser positivos")

    return monedas


def resolver(monedas: list[int]):
    """Devuelve elecciones y puntajes usando el criterio greedy."""
    return juego_monedas_greedy(monedas)


def juego_monedas_greedy(
    monedas: list[int],
) -> tuple[list[tuple[str, int]], int, int]:
    """Devuelve la secuencia de elecciones y los puntajes finales."""
    if not monedas:
        raise ValueError("La entrada debe contener al menos una moneda")
    if any(moneda <= 0 for moneda in monedas):
        raise ValueError("Los valores de las monedas deben ser positivos")
    return _simular_juego(monedas)


def _simular_juego(monedas: list[int]) -> tuple[list[tuple[str, int]], int, int]:
    elecciones = []
    izq = 0
    der = len(monedas) - 1
    puntaje_sophia = 0
    puntaje_mateo = 0

    while izq <= der:
        es_turno_sophia = len(elecciones) % 2 == 0
        toma_izquierda = (
            monedas[izq] >= monedas[der]
            if es_turno_sophia
            else monedas[izq] <= monedas[der]
        )
        if toma_izquierda:
            posicion = "izquierda"
            moneda = monedas[izq]
            izq += 1
        else:
            posicion = "derecha"
            moneda = monedas[der]
            der -= 1

        jugador = "Sophia" if es_turno_sophia else "Mateo"
        elecciones.append((f"{jugador} ({posicion})", moneda))
        if es_turno_sophia:
            puntaje_sophia += moneda
        else:
            puntaje_mateo += moneda

    return elecciones, puntaje_sophia, puntaje_mateo


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Uso: {Path(sys.argv[0]).name} ruta/a/entrada.txt", file=sys.stderr)
        return 2

    try:
        monedas = leer_monedas(sys.argv[1])
        elecciones, puntaje_sophia, puntaje_mateo = resolver(monedas)
        for jugador, moneda in elecciones:
            print(f"{jugador}: {moneda}")
        print(f"Puntaje Sophia: {puntaje_sophia}")
        print(f"Puntaje Mateo: {puntaje_mateo}")
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
