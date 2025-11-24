# Métodos y Funciones de Estructuras de Datos en Python

## 1. Listas (`list`)

  ----------------------------------------------------------------------------------
  Método/Función                Descripción              Ejemplo
  ----------------------------- ------------------------ ---------------------------
  `append(x)`                   Agrega un elemento al    `lista.append(5)`
                                final de la lista.       

  `insert(i, x)`                Inserta un elemento en   `lista.insert(1, "hola")`
                                una posición específica. 

  `extend(iter)`                Agrega los elementos de  `lista.extend([1,2])`
                                otro iterable.           

  `remove(x)`                   Elimina la primera       `lista.remove("hola")`
                                aparición del valor.     

  `pop(i)`                      Elimina y retorna el     `lista.pop(0)`
                                elemento en la posición  
                                dada.                    

  `clear()`                     Vacía la lista.          `lista.clear()`

  `sort()`                      Ordena la lista.         `lista.sort()`

  `reverse()`                   Invierte el orden.       `lista.reverse()`

  `index(x)`                    Retorna la posición del  `lista.index(3)`
                                valor.                   

  `count(x)`                    Cuenta cuántas veces     `lista.count(2)`
                                aparece un valor.        
  ----------------------------------------------------------------------------------

------------------------------------------------------------------------

## 2. Diccionarios (`dict`)

  -------------------------------------------------------------------------------------------
  Método/Función                Descripción              Ejemplo
  ----------------------------- ------------------------ ------------------------------------
  `get(key)`                    Obtiene el valor sin     `d.get("edad")`
                                error si no existe.      

  `keys()`                      Retorna las llaves.      `d.keys()`

  `values()`                    Retorna los valores.     `d.values()`

  `items()`                     Retorna pares (llave,    `d.items()`
                                valor).                  

  `pop(key)`                    Elimina una llave y      `d.pop("nombre")`
                                retorna su valor.        

  `popitem()`                   Elimina un par           `d.popitem()`
                                aleatorio.               

  `update(other)`               Actualiza el             `d.update({"ciudad": "Bogotá"})`
                                diccionario.             

  `clear()`                     Vacía el diccionario.    `d.clear()`

  `setdefault(k, v)`            Retorna valor si existe; `d.setdefault("pais", "Colombia")`
                                si no, lo asigna.        
  -------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 3. Tuplas (`tuple`)

Las tuplas no tienen métodos de modificación porque son inmutables.

  Método       Descripción                              Ejemplo
  ------------ ---------------------------------------- ---------------
  `count(x)`   Cuenta cuántas veces aparece un valor.   `t.count(3)`
  `index(x)`   Retorna la posición del valor.           `t.index(10)`

------------------------------------------------------------------------

## 4. Conjuntos (`set`)

  --------------------------------------------------------------------------------------
  Método/Función                  Descripción              Ejemplo
  ------------------------------- ------------------------ -----------------------------
  `add(x)`                        Agrega un elemento.      `s.add(4)`

  `update(iter)`                  Agrega múltiples         `s.update([1,2])`
                                  elementos.               

  `remove(x)`                     Elimina un elemento      `s.remove(3)`
                                  (error si no existe).    

  `discard(x)`                    Elimina sin error.       `s.discard(10)`

  `pop()`                         Elimina un elemento      `s.pop()`
                                  aleatorio.               

  `clear()`                       Vacía el conjunto.       `s.clear()`

  `union(other)`                  Unión de conjuntos.      `s.union(t)`

  `intersection(other)`           Intersección.            `s.intersection(t)`

  `difference(other)`             Diferencia.              `s.difference(t)`

  `symmetric_difference(other)`   Diferencia simétrica.    `s.symmetric_difference(t)`

  `issubset(other)`               ¿Es subconjunto?         `s.issubset(t)`

  `issuperset(other)`             ¿Es superconjunto?       `s.issuperset(t)`

  `isdisjoint(other)`             ¿No comparten elementos? `s.isdisjoint(t)`
  --------------------------------------------------------------------------------------
