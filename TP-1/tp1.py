"""Interfaz provisional del TP1 de monedas."""

from __future__ import annotations

import sys
from pathlib import Path


def leer_monedas(ruta: str | Path) -> list[int]:
    """Lee valores enteros separados por espacios desde un archivo."""
    contenido = Path(ruta).read_text(encoding="utf-8")
    try:
        monedas = [int(valor) for valor in contenido.split()]
    except ValueError as error:
        raise ValueError("La entrada debe contener únicamente enteros") from error

    if not monedas:
        raise ValueError("La entrada debe contener al menos una moneda")

    return monedas


def resolver(monedas: list[int]):
    """Devuelve la solución del juego de monedas.

    TODO: implementar el algoritmo greedy y definir el formato del resultado.
    """
    raise NotImplementedError("TODO: implementar el algoritmo greedy")


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Uso: {Path(sys.argv[0]).name} ruta/a/entrada.txt", file=sys.stderr)
        return 2

    try:
        monedas = leer_monedas(sys.argv[1])
        resolver(monedas)
    except (OSError, ValueError, NotImplementedError) as error:
        print(f"Pendiente: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
