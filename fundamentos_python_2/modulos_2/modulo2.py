
#! OJOOO, para poder hacer esta importación, debo ir a la terminal y ejecutar el comando
#! python -m modulos_2.modulo2 primero, yendo al paqete raiz, que en este caso es fundamentos_python_2

#? Osea, desde la terminal voy a la carpeta raíz, por ejemplo, si quiero voy a la carpeta principal de
#? este código que es MIS_INICIOS, estando allí, ejecuto el comando python -m carpeta.carpeta.archivo,
#? Reemplazando las palabras carpetas por los nombres de ellas en mi directorio. 
#? En este caso, así: python -m fundamentos_python_2.modulos2.modulo2

#TODO: EXPLICACIÓN. 
#?Esto sucede porque VSC ejecuta por módulos, es decir, este módulo2 es ejecutado solo, no se ejecutan
#? los módulos de las otras carpetas, por lo que la carpeta modulo_1 no se reconoce como parte
#? de esta ruta, entonces debo ir a la raiz fuente desde la que sí se incluya el módulo que quiero importar

from modulos_1.modulo1 import suml, prodl

zeroes = [i for i in range(5)]
ones = [i for i in range(1, 5)]
print(suml(zeroes))
print(prodl(ones))