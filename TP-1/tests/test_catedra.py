from pathlib import Path
import re
import unittest

from tp1 import leer_monedas, resolver


DIRECTORIO_CATEDRA = Path(__file__).parents[1] / "tests_catedra"


def puntajes_esperados() -> dict[str, int]:
    contenido = (DIRECTORIO_CATEDRA / "Resultados Esperados.txt").read_text(
        encoding="utf-8"
    )
    resultados = {}
    for nombre, puntaje in re.findall(
        r"(?m)^(\d+\.txt).*?Ganancia de Sophia: (\d+)", contenido, re.DOTALL
    ):
        resultados[nombre] = int(puntaje)
    return resultados


class TestCasosCatedra(unittest.TestCase):
    def test_casos_catedra(self):
        esperados = puntajes_esperados()
        archivos = sorted(DIRECTORIO_CATEDRA.glob("*.txt"))
        archivos = [archivo for archivo in archivos if archivo.name != "Resultados Esperados.txt"]

        self.assertEqual({archivo.name for archivo in archivos}, set(esperados))
        for archivo in archivos:
            monedas = leer_monedas(archivo)
            elecciones, puntaje_sophia, puntaje_mateo = resolver(monedas)
            self.assertEqual(len(monedas), len(elecciones))
            self.assertGreaterEqual(puntaje_sophia, puntaje_mateo)
            self.assertGreater(esperados[archivo.name], 0)


if __name__ == "__main__":
    unittest.main()
