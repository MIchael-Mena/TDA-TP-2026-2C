# Trabajo Práctico 1: Los Algoritmos Greedy son juegos de niños

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo Greedy. La fecha de entrega del mismo es el 16/09.

## Introducción y primeros años

Cuando Mateo nació, Sophia estaba muy contenta. Finalmente tendría un hermano con quien jugar. Sophi tenía 3 años cuando Mateo nació. Ya desde muy chicos, ella jugaba mucho con su hermano.

Pasaron los años, y fueron cambiando los juegos. Cuando Mateo cumplió 4 años, el padre de ambos le explicó un juego a Sophia: Se dispone una fila de \(n\) monedas, de diferentes valores. En cada turno, un jugador debe elegir alguna moneda. Pero no puede elegir cualquiera: sólo puede elegir o bien la primera de la fila, o bien la última. Al elegirla, la remueve de la fila, y le toca luego al otro jugador, quien debe elegir otra moneda siguiendo la misma regla. Siguen agarrando monedas hasta que no quede ninguna. Quien gane será quien tenga el mayor valor acumulado (por sumatoria).

El problema es que Mateo es aún pequeño para entender cómo funciona esto, por lo que Sophia debe elegir las monedas por él. Digamos, [Mateo está “jugando”](https://youtu.be/5cZqe90zxNE?t=20). Aquí surge otro problema: Sophia es muy competitiva. Será buena hermana, pero no se va a dejar ganar (consideremos que tiene 7 nada más). Todo lo contrario. En la primaria aprendió algunas cosas sobre algoritmos greedy, y lo va a aplicar.

### Consigna

1. [**Obligatorio**] Hacer un análisis del problema, y proponer un algoritmo greedy que obtenga **la solución óptima** al problema planteado: Dados los \(n\) valores de todas las monedas, indicar qué monedas debe ir eligiendo Sophia para si misma y para Mateo, de tal forma que se asegure de **ganar siempre**. Considerar que Sophia siempre comienza (para sí misma).
2. [**Obligatorio**] Demostrar que el algoritmo planteado obtiene siempre la solución óptima (desestimando el caso de una cantidad par de monedas de mismo valor, en cuyo caso siempre sería empate más allá de la estrategia de Sophia).
3. [**Obligatorio**] Escribir el algoritmo planteado. Describir y justificar la complejidad de dicho algoritmo. Analizar si (y cómo) afecta la variabilidad de los valores de las diferentes monedas a los tiempos del algoritmo planteado.
4. [**Opcional**] Analizar si (y cómo) afecta la variabilidad de los valores de las diferentes monedas a la optimalidad del algoritmo planteado.
5. [**Opcional**] Realizar ejemplos de ejecución para encontrar soluciones y corroborar lo encontrado. Adicionalmente, el curso proveerá con algunos casos particulares que deben cumplirse su optimalidad también.
6. [**Opcional**] Hacer mediciones de tiempos para corroborar la complejidad teórica indicada. Agregar los casos de prueba necesarios para dicha corroboración. Esta corroboración empírica debe realizarse confeccionando gráficos correspondientes, y utilizando la técnica de cuadrados mínimos. Para esto, [proveemos una explicación detallada](https://github.com/algoritmos-rw/tda_ejemplos/blob/main/analisis_complejidad/cuadrados_minimos.ipynb), en conjunto de ejemplos.
7. [**Opcional**] Agregar cualquier conclusión que les parezca relevante.

## Entrega

Completar el [formulario de entrega](https://forms.gle/4rvJjDA3cEq1AqTG9) con los integrantes y el link al repositorio donde se encuentre el código fuente, y donde debe encontrarse el informe en formato PDF.

La forma de ejecutar el programa debe ser:

```plaintext
./tp1 ruta/a/entrada.txt
```

O bien:

```plaintext
python3 tp1.py ruta/a/entrada.txt
```

El formato a ser aceptado debe ser como los ejemplos dado por el curso. El formato de salida debe ser parecido a los ejemplos de salidas brindados. No es necesario que sea exactamente igual, y pueden modificar algo en función de lo que analicen, pero debe mantenerse similar.

**Importante**: en caso que lo descripto no se cumpla, el trabajo será enviado automáticamente para reentrega sin otra corrección mediante, ya que lo primero que hacemos es verificar que el programa funcione.

El informe debe ser:

* Autocontenido: es decir, no debe ser necesario ponernos a buscar el código por diferentes lugares. El código que debe ser incluido es el código de los algoritmos a desarrollar (no es de interés un `main`, o el procesamiento de archivos, sino los algoritmos principales), y estos deben estar incluidos donde consideren correcto dado el desarrollo del informe, para su entendimiento.
* Tener todo el análisis correspondiente.
* Ser realizado en un formato profesional. Para esto, les brindamos [un template](https://www.overleaf.com/read/bhwnwxxbmdhp) en \(\LaTeX\) para que puedan utilizar (también se encuentra en [la *home* del sitio web del curso](https://algoritmos-rw.github.io/tda_bg)). No es necesario que lo sigan al pie de la letra, es simplemente un ejemplo que tiene varias cosas que pueden llegar a utilizar de \(\LaTeX\). Si ya conocen \(\LaTeX\) no es necesario que lo utilicen, o mismo si utilizan algún otro formato (e.g. Markdown con Pandoc), pero recomendamos su revisión para que vean cosas que no deben de faltar. Por supuesto, pueden trabajar localmente como usar Overleaf o cualquier otra herramienta. El objetivo de darles el template no es la de limitar la creatividad, sino de asegurarnos que se cumplan lineamientos básicos sobre lo que se espera de una entrega de un informe en la facultad.
* En caso de ser necesarias reentregas, **agregar las modificaciónes en un Anexo al final del informe**. No modificar lo hecho anteriormente. La excepción a esto sería si hay que rehacer una enorme mayoría de lo escrito.

La nota del trabajo práctico tendrá en cuenta tanto la presentación y calidad de lo presentado, como también el desarrollo del trabajo. No será lo mismo un trabajo realizado con lo mínimo indispensable, que uno bien presentado, analizado, y probado con diferentes volúmenes, *set* de datos, o estrategias de generación de *sets*, en el caso que corresponda.

Sobre puntos obligatorios y opcionales:

* La idea de hacer electivos algunos puntos es que aquellos grupos que consideren que estos trabajos no hacen a su formación, simplemente hagan lo mínimo, y quienes consideren que este desarrollo les puede aportar (especialmente para materias futuras) o bien quieran resolver un problema utilizando lo visto en la materia, tengan un lugar para hacerlo.
* Los puntos opcionales no son necesarios para aprobar, pero cada uno contribuye a tener mejor nota.
* En caso que los puntos obligatorios no estén aprobables, se reenviará a reentrega. Si un punto opcional no está aprobable simplemente se considerará para la nota del trabajo práctico (eventualmente, según el detalle de lo que corresponda, podría reentregarse para mejorar nota).
* Para la fecha de entrega, los puntos obligatorios deben estar hechos. En caso de no hacerse, se dará una única semana (sin posibilidad de extensión) para que estos puntos (y solo estos, no los electivos) estén completados para tener un máximo de 4 de nota, y en caso de no encontrarse en condiciones de aprobar, el trabajo quedará desaprobado (y de allí la cursada).
* Los puntos opcionales que no hayan estado implementados para la fecha de entrega, no se podrán implementar en una “reentrega” o a futuro. El trabajo práctico no se hace en cuotas. Si hay algo para ser corregido de un punto opcional ya hecho, se puede corregir eventualmente.
