import tempfile
import unittest
from pathlib import Path

from tp1 import leer_monedas, resolver


class TestLeerMonedas(unittest.TestCase):
    def escribir_temporal(self, contenido: str) -> Path:
        archivo = tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", delete=False
        )
        archivo.write(contenido)
        archivo.close()
        self.addCleanup(lambda: Path(archivo.name).unlink(missing_ok=True))
        return Path(archivo.name)

    def test_lee_valores_separados_por_espacios(self):
        ruta = self.escribir_temporal("5 10 20 1")
        self.assertEqual(leer_monedas(ruta), [5, 10, 20, 1])

    def test_lee_valores_separados_por_punto_y_coma(self):
        ruta = self.escribir_temporal("5;10;20;1")
        self.assertEqual(leer_monedas(ruta), [5, 10, 20, 1])

    def test_ignora_comentarios(self):
        ruta = self.escribir_temporal("# comentario\n5; 10; 20")
        self.assertEqual(leer_monedas(ruta), [5, 10, 20])

    def test_rechaza_entrada_vacia(self):
        ruta = self.escribir_temporal("# sin monedas")
        with self.assertRaises(ValueError):
            leer_monedas(ruta)

    def test_rechaza_valores_no_positivos(self):
        ruta = self.escribir_temporal("5 0 -2")
        with self.assertRaises(ValueError):
            leer_monedas(ruta)


class TestResolver(unittest.TestCase):
    def test_casos_borde_y_puntajes(self):
        casos = {
            (7,): (7, 0),
            (2, 9): (9, 2),
            (1, 5, 2, 10, 6): (21, 3),
            (4, 1, 8, 3): (12, 4),
        }
        for monedas, puntajes in casos.items():
            elecciones, sophia, mateo = resolver(list(monedas))
            self.assertEqual((sophia, mateo), puntajes)
            self.assertEqual(len(elecciones), len(monedas))

    def test_empate_con_valores_repetidos(self):
        elecciones, sophia, mateo = resolver([1, 2, 2, 1])
        self.assertEqual((sophia, mateo), (3, 3))
        self.assertEqual(len(elecciones), 4)

    def test_elecciones_respetan_extremos_y_criterio_greedy(self):
        monedas = [5, 1, 4, 2, 9]
        elecciones, sophia, mateo = resolver(monedas)
        izquierda = 0
        derecha = len(monedas) - 1

        for turno, (descripcion, valor) in enumerate(elecciones):
            es_turno_sophia = turno % 2 == 0
            posicion = "izquierda" if "izquierda" in descripcion else "derecha"
            self.assertIn(valor, (monedas[izquierda], monedas[derecha]))
            if es_turno_sophia:
                self.assertEqual(valor, max(monedas[izquierda], monedas[derecha]))
            else:
                self.assertEqual(valor, min(monedas[izquierda], monedas[derecha]))

            if posicion == "izquierda":
                izquierda += 1
            else:
                derecha -= 1

        self.assertEqual(sophia + mateo, sum(monedas))
        self.assertGreaterEqual(sophia, mateo)

    def test_rechaza_lista_vacia_y_valores_no_positivos(self):
        with self.assertRaises(ValueError):
            resolver([])
        with self.assertRaises(ValueError):
            resolver([3, 0, 2])
        with self.assertRaises(ValueError):
            resolver([3, -1, 2])


if __name__ == "__main__":
    unittest.main()
