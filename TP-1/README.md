# Teoría de Algoritmos

## Trabajo Práctico 1

TP1 del segundo cuatrimestre de 2026: [Los Algoritmos Greedy son juegos de
niños](https://algoritmos-rw.github.io/tda_bg/tps/2026_2/tp1/).

El programa debe elegir monedas únicamente desde el primero o el último lugar
de una fila. Sophia comienza y también decide las elecciones de Mateo. Se debe
informar la secuencia de elecciones y el total acumulado por cada jugador.

## Informe

El informe se encuentra en documento PDF `informe_tp1.pdf`

## Estructura de los tests

- `tests_catedra/`: entradas manuales y casos que entregue la cátedra.
- `tests/`: suite automatizada de Python.

## Ejecución

Desde la raíz del proyecto, crear y activar el entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows PowerShell, activar el entorno con:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si existe `requirements.txt`, instalar sus dependencias con:

```bash
python3 -m pip install -r requirements.txt
```

Ejecutar el programa indicando un archivo de entrada:

```bash
python3 tp1.py tests_catedra/ejemplo.txt
```

Ejecutar la suite automatizada con:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```