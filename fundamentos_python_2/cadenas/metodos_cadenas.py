





#TODO: Métodos de Formato y Modificación

#! capitalize()
#? Convierte el primer carácter de la cadena a mayúscula y el resto a minúscula.

# s = "hola mundo"
# print(s.capitalize())  #? ---> "Hola mundo"


#! casefold()
#? Convierte la cadena a minúsculas para comparaciones insensibles a mayúsculas/minúsculas. Esta es útil para
#? caracteres especiales en idiomas diferentes como alemán o turco que tienen sus caracteres especiales

# s = "MÜNCHEN"
# print(s.casefold())  #? ---> "münchen"


#! center(width, fillchar=' ')
#? Centra la cadena dentro de un ancho especificado en el primer argumento, rellenando con un carácter 
#? opcional especificado en el segundo argumento (Si no se pone un segundo argumento, solo centra la cadena).

# s = "python"
# print(s.center(10))  #? ---> "  python  "

# s = "python"
# print(s.center(10, '-'))  #? ---> "--python--"


#! ljust(width, fillchar=' ')
#? Tira la cadena a la izquierda dentro de un ancho especificado y el espacio que queda a la derecha lo llena
#? con el caracter indicado, (Si no se pone un segundo argumento, solo tira la cadena a la izquierda).

# s = "python"
# print(s.ljust(10))       #? --->   "python    "

# s = "python"
# print(s.ljust(10, '-'))  #? --->   "python----"


#! rjust(width, fillchar=' ')
#? Tira la cadena a la derecha dentro de un ancho especificado y el espacio que queda a la izquierda lo llena
#? con el caracter indicado, (Si no se pone un segundo argumento, solo tira la cadena a la derecha).

# s = "python"
# print(s.rjust(10))       #? ---> "    python"

# s = "python"
# print(s.rjust(10, '-'))  #? ---> "----python"

#! zfill(width)
#? Rellena con ceros a la izquierda hasta alcanzar un ancho especificado, osea, lo que esto hace es poner 
#? ceros a la izquierda de la cadena. 

# s = "42"
# print(s.zfill(5))       #? ---> "00042"


#TODO: Métodos de Transformación:

#! lower()
#? Convierte todos los caracteres de la cadena a minúsculas.

# s = "HELLO"
# print(s.lower())  #? ---> "hello"


#! upper()
#? Convierte todos los caracteres de la cadena a mayúsculas.

# s = "hello"
# print(s.upper())  #? ---> "HELLO"


#! swapcase()
#? Intercambia mayúsculas por minúsculas y viceversa.

# s = "Hello WorLd"
# print(s.swapcase())  #? ---> "hELLO wORlD"


#! title()
#? Convierte el primer carácter de cada palabra a mayúscula.

# s = "hello world"
# print(s.title())  #? ---> "Hello World"


#TODO: Métodos de Búsqueda

#! find(sub, start=0, end=len(s))
#? Busca un substring y devuelve la posición inicial o -1 si no lo encuentra.

# s = "hello world"
# print(s.find("world"))  #? ---> 6


#! rfind(sub, start=0, end=len(s))
#? Busca un substring desde el final y devuelve la posición inicial o -1 si no lo encuentra.  Osea, este
#? busca la subcadena pasada como argumento, pero desde atrás hacia adelante. 

# s = "hello world world"
# print(s.rfind("world"))   #? ---> 12 || Al buscar de derecha a izquierda la primera aparición está en el
                            #? índice 12


#! index(sub, start=0, end=len(s))
#? Busca un substring y devuelve la posición inicial; lanza una excepción si no lo encuentra. Osea, es lo
#? mismo que el find, pero, este arroja un error si no lo encuentra. 

# s = "hello world"
# print(s.index("world"))   #? ---> 6 || Al buscar de izquierda a derecha la primera aparición está en el
                            #? índice 6


#! rindex(sub, start=0, end=len(s))
#? Busca un substring desde el final y devuelve la posición inicial; lanza una excepción si no lo encuentra.

# s = "hello world world"
# print(s.rindex("world"))  #? ---> 12 || Al buscar de derecha a izquierda la primera aparición está en el
                            #? índice 12


#! count(sub, start=0, end=len(s))
#? Cuenta cuántas veces aparece un substring en la cadena.

# s = "hello world world"
# print(s.count("world"))  #? ---> 2 || Porque la subcadena world aparece dos veces en la cadena original. 


#TODO: Métodos de Verificación:

#! isalnum()
#? Verifica si la cadena contiene solo caracteres alfanuméricos (sin espacios ni símbolos).

# s = "hello123"
# print(s.isalnum())  #? ---> True || Porque sí es cierto que tiene números o letras

# s = "hello 123"           
# print(s.isalnum())  #? ---> False || Porque no es cierto que tiene solo números o letras, también tiene espacio.  


#! isalpha()
#? Verifica si la cadena contiene solo letras.

# s = "hello"
# print(s.isalpha())    #? ---> True   || Porque sí es cierto que solo tiene letras

# s = "hello123"
# print(s.isalpha())      #? --->  False || Porque no es cierto que solo tiene letras, también tiene números


#! isdigit()
#? Verifica si la cadena contiene solo dígitos.

# s = "123"
# print(s.isdigit())  #? True || Todos los caracteres de la cadena son dígitos numéricos solamente. 

# s = "123 a"
# print(s.isdigit())  #? False || NO todos los caracteres son números, hay un espacio y una letra. 


#! islower()
#? Verifica si todos los caracteres alfabéticos de la cadena están en minúsculas.

# s = "hello"
# print(s.islower())    #? ---> True || Todos están en minúscula

# s = "Hello"
# print(s.islower())      #? ---> False || La H está en mayúscula


#! isupper()
#? Verifica si todos los caracteres de la cadena están en mayúsculas.

# s = "HELLO"
# print(s.isupper())      #? ---> True || Todos están en mayúscula

# s = "HELLo"
# print(s.islower())      #? ---> False || No todos están en mayúscula, la o está en minúscula

#! isspace()
#? Verifica si la cadena contiene solo espacios.

# s = "   "
# print(s.isspace())  #? ---> True || La cadena solamente tiene espacios. 

# s = "   h"
# print(s.isspace())  #? ---> False || La cadena no solo tiene espacios, hay una h. 


#! istitle()
#? Verifica si la cadena está en formato título (cada palabra con la primera letra mayúscula).

# s = "Hello World"
# print(s.istitle())  #? ---> True || Porque todas las palabras de la cadena inician en mayúscula

# s = "Hello world"
# print(s.istitle())  #? ---> False || Porque la segunda palabra no inicia en mayúscula


#TODO: Métodos de División y Unión

#! split(sep=None, maxsplit=-1)
#? Divide la cadena en una lista usando un separador.

# s = "hello world"
# print(s.split())  #? ---> ['hello', 'world']


#! rsplit(sep=None, maxsplit=-1)
#? Divide desde el final.

# s = "a,b,c"
# print(s.rsplit(",", 1))  #? ---> ['a,b', 'c']


#! join(iterable)
#? Une los elementos de un iterable en una cadena usando un separador.

# l = ['hello', 'world']
# print(" ".join(l))  #? ---> "hello world"


#! partition(sep)
#? Divide la cadena en tres partes: antes, el separador, después.

# s = "hello world for ever"
# print(s.partition(" "))  #? ---> ('hello', ' ', 'world for ever')


#! rpartition(sep)
#? Igual que partition, pero desde el final.

# s = "hello world for ever"
# print(s.rpartition(" "))  #? ---> ('hello world for', ' ', 'ever')


#TODO: Otros Métodos
#! replace(old, new, count=-1)
#? Reemplaza partes de la cadena.

# s = "hello world"
# print(s.replace("world", "Python"))  #? ---> "hello Python"


#! strip(chars=None)
#? Elimina caracteres del inicio y final.

# s = "  hello  "
# print(s.strip())  #? ---> "hello"


#! lstrip(chars=None)
#? Elimina caracteres del inicio.

# s = "  hello"
# print(s.lstrip())  #? ---> "hello"


#! rstrip(chars=None)
#? Elimina caracteres del final.

# s = "hello  "
# print(s.rstrip())  #? ---> "hello"


#! startswith(prefix, start=0, end=len(s))
#? Verifica si la cadena empieza con un prefijo.

# s = "hello world"
# print(s.startswith("hello"))  #? ---> True


#! endswith(suffix, start=0, end=len(s))
#? Verifica si la cadena termina con un sufijo.

# s = "hello world"
# print(s.endswith("world"))  #? ---> True