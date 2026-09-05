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

Cada entrada contiene una única línea con valores enteros separados
por espacios. Por ejemplo, `tests_catedra/ejemplo.txt` contiene:

```text
1 5 2 10 6
```

Los casos de prueba deben respetar este formato, salvo que la cátedra publique
un formato específico diferente.

## Casos que deben cubrirse

Como mínimo, la suite debe incluir:

1. Una moneda.
2. Dos monedas.
3. Cantidad impar de monedas.
4. Cantidad par de monedas.
5. Valores repetidos y empates en los extremos.
6. Valores ordenados, inversamente ordenados y valores grandes.
7. Los casos particulares provistos por la cátedra.

Para cada caso conviene verificar que todas las elecciones sean legales, que
cada moneda se use una sola vez, que las sumas coincidan con las elecciones y
que se cumpla el resultado esperado. En empates no se debe exigir una única
secuencia si existen varias soluciones equivalentes. Para casos pequeños,
conviene comparar el resultado del greedy contra una solución de referencia
exhaustiva que pruebe todas las elecciones posibles; así se puede verificar la
optimalidad sin depender de resultados escritos a mano.

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