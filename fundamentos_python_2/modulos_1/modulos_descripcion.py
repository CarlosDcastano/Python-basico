
#!                                     __  __   ___   ____   _    _   _       ___    _____  
#!                                    |  \/  | / _ \ |  _ \ | |  | | | |     / _ \  |  ___| 
#!                                    |      || | | || | | || |  | | | |    | | | | | |___  
#!                                    | |\/| || | | || | | || |  | | | |    | | | | | __  | 
#!                                    | |  | || |_| || |_| || |__| | | |___ | |_| |  ___| | 
#!                                    |_|  |_| \___/ |____/  \____/  |_____| \___/  |_____|  

#TODO:                                  DEFINICIONES Y PUNTOS IMPORTANTES:

#? Estos módulos son los que están directamente en el paquete de python preinstalados, solo que para poder usarlos,
#? debo importarlos a mi proyecto a medida que los necesite, es decir, no está incluídos en mi código por sí solos, 
#? sino que debo llamar el módulo a mi archivo, si quiero hacer uso de alguna de sus funciones, constantes o variables

#! Importante: Cuando importo un módulo a un archivo de mi proyecto, si necesito usar ese módulo en otro archivo
#! debo importarlo también en ses otro archivo. 

#TODO:                                    SINTAXIS PARA IMPORTAR MÓDULOS:

#? Tengo tres formas de importar los módulos, la primera es importando el módulo completo, para lo cual, si quiero
#? usar alguna entidad de dicho módulo, debo decir el nombre del módulo.entidad, así:

#TODO: Importar todo el módulo:
# import math               #? Aquí importamos todo el módulo de ma

# x = 5                     #? Creo una variable normal en mi código
# print(math.sqrt(x))       #? Si quiero usar la función sqrt del módulo math, primero debo decir el nombre del
                            #? módulo math seguido por un . y luego el nombre de la entidad que usaré, aquí sqrt. 

#TODO: Importar una entidad específica del módulo:

# from math import sqrt       #? Aquí importamos de math, solo la función de raiz cuadrada sqrt

# x = 5                       #? Creo una variable normal en mi código
# print(f"{sqrt(x)}")         #? Ahora no necesito nombrar el nombre del módulo, sino solo la función sqrt
# print(f"{sin(x)}")          #? Aquí se marca un error, porque sin no fue importado de math, solo sqrt      
# print(f"{math.sin(x)}")     #? ESto tampoco funcionará ni aún nombrando el módulo. 

#! OJoooooo, también puedo importar las entidades que quiera de un módulo. 

# from math import sqrt, sin, cos   #? Aquí estoy importanto tres entidades del módulo math en una sola línea

# x = 5                             #? Creo una variable normal en mi código
# print(f"{sqrt(x)}")               #? Ahora no necesito nombrar el nombre del módulo, sino solo la función sqrt
# print(f"{sin(x)}")                #? Aquí sí funciona sin, porque también fue llamado al importar math      
# print(f"{cos(x)}")                #? Adicionalmente importamos la función cos y funciona

                        #TODO: Palabra clave as
                            #? Si no quiero que mi entidad importada entre en conflicto con alguna entidad de mi 
                            #? código, puedo importarla con un alias usando la palabra reservada as, así:

# from math import sqrt as sq, sin as s #? Importo desde math la entidad sqrt, pero le cambio su nombre por sq
                                        #? de hecho puedo poner varios alias a varias entidades en la misma línea

# x = 5                             #? Creo una variable normal en mi código
# print(f"{sqrt(x)}")               #? sqrt pero no se reconoce porque el nombre es diferente pues ya se llama sq
# print(f"{sq(x)}")                 #? sq sí se reconoce pues es el alias que le puse a sqrt

                        #TODO: También se usa directamente por cada módulo. 
                            #? También puedo ponerle un alias al módulo en sí, por ejemplo:

import math as m                    #? Importo math, pero le pongo un alias convirtiéndola en m 

x = 5                               #? Creo una variable local 
print(f"{m.sin(x)}")                #? ahora uso la entidad sin, pero invocando primero el módulo como m


#TODO: Importar todas las entidades de un módulo:
#? Cuando no quiero específicar una entidad propiamente a importar, sino que quiero que todas las entidades de 
#? ese módulo sean importadas, solo se indica que de ese módulo quiero importarlo todo, con un *

#! NOTA: Es funcional, pero hace mi código más pesado y además, puede causar conflicto con nombre de variables
#! o funciones propias de mi código. 

# from math import *                #? Aquí del módulo math, importo absolutamente todas las intancias

# x = 5                             #? Creo una variable normal en mi código
# print(f"{sqrt(x)}")               #? Ahora no necesito nombrar el nombre del módulo, sino solo la función sqrt
# print(f"{sin(x)}")                #? Aquí sí funciona sin, porque todo de math fue importado      
# print(f"{cos(x)}")                #? Adicionalmente importamos la función cos y funciona. 

#! ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#TODO: ALGO CLAVE PARA CONOCER MIS MÓDULOS IMPORTADOS: La función dir()
#? Esta nos enlista todas las entidades en orden alfaético contiene el módulo que le pasamos como argumento a nuestra
#? función dir() OJO, para esto, primero tenemos que importar el módulo del que queremos conocer sus entidades, además,
#? si dicho módulo fue importado con un alias, el argumento que debemos pasarle a dir() es el alias, así:

# import math as m

# print(dir(m))   #? ---> ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 
                #? 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees',
                #? 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp',
                #? 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 
                #? 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 
                #? 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

#TODO: Ejemplo del módulo random y algunas de sus funciones.

from random import randrange, randint

print(randrange(5), end=' ') # Trae un valor aleatorio desde 0 hasta 5, sin contar el 5
print(randrange(8, 18))      # Trae un valor aleatorio entre el 8 y el 18, sin contar el 18
print(randrange(0, 9, 1))    # Trae un valor aleatorio entre 0 y 9, con un incremento a 1
print(randint(0, 6))         # Trae un valor aleatorio de 0  a 6, contando el 6

#TODO: ESTOS SON TODOS LOS MÓDULOS DE PITHON CON UNA BREVE DESCRIPCIÓN:

#TODO: 1. Tipos de datos y estructuras
#? array
#? collections
#? dataclasses
#? enum
#? types
#? typing

#TODO: 2. Matemáticas y números
#? cmath
#? decimal
#? fractions
#? math
#? numbers
#? random
#? statistics

#TODO: 3. Manejo de fechas y tiempos
#? calendar
#? datetime
#? time
#? zoneinfo (desde Python 3.9)

#TODO 4. Programación funcional
#? functools
#? itertools
#? operator

#TODO: 5. Manejo de texto y cadenas
#? codecs
#? re
#? string
#? textwrap
#? unicodedata

#TODO: 6. Manejo de archivos, directorios y entorno
#? filecmp
#? fileinput
#? fnmatch
#? glob
#? linecache
#? os
#? os.path
#? pathlib
#? platform 
#? shutil
#? stat
#? tempfile

#TODO: 7. Persistencia y bases de datos
#? dbm
#? sqlite3
#? pickle
#? shelve

#TODO: 8. Compresión y archivado
#? bz2
#? gzip
#? lzma
#? tarfile
#? zipfile

#TODO: 9. Formatos de archivo y protocolos
#? configparser
#? csv
#? json
#? plistlib
#? xml

#TODO: 10. Internet y protocolos de red
#? ftplib
#? http
#? imaplib
#? nntplib
#? poplib
#? smtplib
#? socket
#? ssl
#? urllib
#? xmlrpc

#TODO: 11. Seguridad y cifrado
#? hashlib
#? hmac
#? secrets
#? ssl

#TODO: 12. Procesos, hilos y concurrencia
#? concurrent.futures
#? multiprocessing
#? subprocess
#? threading

#TODO: 13. Desarrollo y depuración
#? argparse
#? contextlib
#? faulthandler
#? pdb
#? traceback
#? unittest

#TODO: 14. Utilidades del intérprete
#? ast
#? code
#? dis
#? inspect
#? site
#? sys
#? warnings

#TODO: 15. Manejo de módulos
#? importlib
#? pkgutil
#? zipimport

#! PARA CONOCER MÁS SOBRE CADA MÓDULO EN ESPECÍFICO Y CONOCER SUS ENTIDADES, DEJO ESTE PRINT CON LA FUNCIÓN DE
#! PYTHON INTEGRADA dir(), DE MODO QUE PUEDA INVESTIGAR LAS ENTIDADES DE ESTOS MÓDULOS:

import importlib               #? REcuerda cambiar el módulo que quieres investigar. 
print(f"{dir(importlib)}")     #? Pasar el módulo que quiero como argumento. 