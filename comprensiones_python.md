# Comprensiones en Python: Uso, Comparación y Ejemplos

Las **comprensiones** (`list comprehension`, `set comprehension`,
`dict comprehension` y expresiones generadoras) son una forma compacta,
eficiente y legible de crear estructuras de datos en una sola línea,
comparado con el formato tradicional que usa indentación y bucles `for`.

------------------------------------------------------------------------

# 1. ¿Qué es una comprensión?

Es una expresión como:

``` python
[p for p in productos if p["nombre"] == nombre_ingresado]
```

que reemplaza:

``` python
resultado = []
for p in productos:
    if p["nombre"] == nombre_ingresado:
        resultado.append(p)
```

------------------------------------------------------------------------

# 2. Ventajas de las comprensiones

-   Más cortas y expresivas.\
-   Más rápidas en ejecución.\
-   Eliminan el uso de `append()`.\
-   Facilitan filtrados y transformaciones en una sola línea.

------------------------------------------------------------------------

# 3. Comprensiones de Listas

## 3.1 Ejemplo básico

### Forma tradicional

``` python
numeros = []
for n in range(5):
    numeros.append(n)
```

### Con comprensión

``` python
numeros = [n for n in range(5)]
```

------------------------------------------------------------------------

## 3.2 Con filtro `if`

### Tradicional

``` python
pares = []
for n in range(10):
    if n % 2 == 0:
        pares.append(n)
```

### Con comprensión

``` python
pares = [n for n in range(10) if n % 2 == 0]
```

------------------------------------------------------------------------

## 3.3 Transformaciones aplicadas

``` python
cuadrados = [n**2 for n in range(6)]
```

------------------------------------------------------------------------

## 3.4 Condición ternaria dentro de la comprensión

``` python
etiquetas = ["par" if n % 2 == 0 else "impar" for n in range(6)]
```

------------------------------------------------------------------------

## 3.5 Comprensión anidada (tipo matriz)

### Tradicional

``` python
resultado = []
for fila in range(3):
    for col in range(3):
        resultado.append((fila, col))
```

### Con comprensión

``` python
resultado = [(fila, col) for fila in range(3) for col in range(3)]
```

------------------------------------------------------------------------

# 4. Comprensiones de Diccionarios

## 4.1 Ejemplo simple

``` python
cuadrados = {n: n*n for n in range(5)}
```

------------------------------------------------------------------------

## 4.2 Con filtro

``` python
mayores = {k: v for k, v in {"a":5,"b":2,"c":8}.items() if v > 4}
```

------------------------------------------------------------------------

# 5. Comprensiones de Conjuntos

``` python
unicos_pares = {n for n in range(10) if n % 2 == 0}
```

------------------------------------------------------------------------

# 6. Expresiones generadoras (generator expressions)

Son como comprensiones pero usan **()** y generan los valores de uno en
uno, más eficientes en memoria.

``` python
gen = (n*n for n in range(5))
```

------------------------------------------------------------------------

# 7. Ejemplos avanzados y complejos

## 7.1 Filtrar diccionarios dentro de listas

``` python
filtrados = [p for p in productos if p["categoria"] == "tecnologia"]
```

------------------------------------------------------------------------

## 7.2 Transformar valores dentro de diccionarios

``` python
precios_con_descuento = [
    {**p, "precio": p["precio"] * 0.9}
    for p in productos
]
```

------------------------------------------------------------------------

## 7.3 Comprensión con múltiples condiciones

``` python
filtrados = [
    p for p in productos
    if p["stock"] > 0 and p["precio"] <= 50000
]
```

------------------------------------------------------------------------

## 7.4 Comprensiones anidadas complejas

``` python
matriz = [
    [fila * col for col in range(1, 6)]
    for fila in range(1, 6)
]
```

------------------------------------------------------------------------

## 7.5 Diccionarios construidos desde listas de diccionarios

``` python
productos_por_id = {p["id"]: p for p in productos}
```

------------------------------------------------------------------------

# 8. Conclusión

Las comprensiones permiten escribir código más limpio, compacto y
eficiente.\
Desde la simple creación de listas hasta transformaciones complejas de
datos, son una herramienta fundamental en Python moderno.
