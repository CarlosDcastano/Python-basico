
#? La idea es explicar el funcionamiento básico y avanzado de las cadenas. para esto, se debe identificar cómo
#? las computadoras identifican los caracteres y para resumir todo un mundo de explicaciones teóricas,
#? simplemente, es el hecho de que internacionalmente hay un estandar en el que a cada caracter, se le
#? asigna un nuúmero, por ejemplo, el espacio es en sí un caracter, y es el 32, la letra a minúscula es el
#? 97 y así sucesivamente.

#TODO: Conocer el valor del punto de código. 
#? Si deseo conocer el valor de un caracter, hay una función para ello, conocida como ord() 

# ch = "c"
# print(f"{ord(ch)}") #? ---> 99 || Imprime el punto de código asignado a dicho caracter

#TODO: Conocer el caracter asignado a un punto de código. 
#? Si quiero hacer lo contrario, es decir, escribir el punto de código y que me traiga el caracter correspondiente. 

# print(f"{chr(99)}")  #? ---> c ||  Imprime el caracter asignado a dicho código

#! Las cadenas pueden ser de varios renglones, sea con tres comillas simples o tres comillas dobles, así:

# multiline = """hola, esto
# es una cadena multi                 #? No importa si tiene varios renglones, funciona porque tiene
# línea"""                            #? tres comillas al iniciar y al finalizar la cadena

# print(f"""{len(multiline)}          #? Incluso si traigo variables o funciones dentro de mis tres comillas
# La idea es que esto funcione""")

#TODO: Cadenas como listas: 
#? Las cadenas tienen ciertos comportamientos que la asemejan a una lista, por ejemplo, se puede mirar su
#? tamaño, se puede traer un caracter por su índice, también se puede hacer slicing o "Rebanada"

#TODO: Mirar el mamaño
# cadena = "Esto es una cadena"     #? ---> 18 || Esta cadena tiene 18 caracteres, contando espacios
# print(len(cadena))

#TODO: Traer un caracter por su índice
# cadena = "Esto es una cadena"
# print(cadena[6])                #? ---> s || ya que s ocupa el índice 6 en la cadena

#TODO: Hacer slicing a la cadena
# cadena = "Esto es una cadena"
# print(cadena[0:3])              #? ---> Est
# print(cadena[5:10])             #? ---> es un

#TODO: Uso de operadores in and not in. 
#? Al igual que con las listass, también puedo saber si un caracter se encuentra o no en una cadena de 
#? caracteres, arrojará True o False. 

# cadena = "Esto es una cadena"
# print("e" in cadena)            #? ---> True  || Porque es cierto que e sí está en la cadena
# print("e" not in cadena)        #? ---> False || Porque es falso que e no está en la cadena

#TODO: Uso de función min y max:
#? Esta función se aplica también a las listas, lo que hace min() es hallar el valor menor en la lista o
#? cadena y max() hace lo contrario, halla el valor mayor en estas. 
#! NOTA: El orden de quien es mayor o menor, lo da la tabla ASCII, la tabla estandar que le da valor a los
#! caracteres. 

# cadena = "Esto es una cadena"
# print(f"{min(cadena)}")             #? ---> El resultado es un espacio vacío, pues el caracter menor
#                                     #? es justamente el espacio (NO OLVIDAD, LOS ESPACIOS TAMBIÉN CUENTAN)

# cadena = "Esto es una cadena"       
# print(f"{max(cadena)}")             #? ---> En esta cadena el caracter mayor es la u

#TODO: Funcion list():
#? Recordemos que la función lista convierte un iterable a una lista, como una cadena se puede iterar,
#? entonces también puedo convertirla a una lista. 

# cadena = "Esto es una cadena"

# lista = list(cadena)    #? Creo una lista y le almaceno lo que da la función list con el argumento cadena
# print(f"{lista}")  #? ---> ['E', 's', 't', 'o', ' ', 'e', 's', ' ', 'u', 'n', 'a', ' ', 'c', 'a', 'd', 'e', 'n', 'a']

#TODO: Método .count(x):
#? Retorna la cantidad de veces que x aparece en la cadena

cadena = "Esto es una cadena"

print(cadena.count("e"))        #? ---> 2 || Solo hay dos e minúsculas, recordar que se hace diferencia entre
                                #? mayúsculas y menúsculas



#TODO: Método .index(x)
#? Al igual que en las listas, también puedo usar el método index(x) que lo que hace es traerme el índice 
#? (O sea la posición en la lista o cadena) en la que se encuentra el elemento o caracter x que paso como
#? argumento. NOTA:::::: Trae solo la primera aparición de dicho caracter o elemento. 

# cadena = "Esto es una cadena"
# print(cadena.index("E"))    #? ---> 0 || Porque la E mayúscula está en el índice 0 de la cadena
# print(cadena.index("e"))    #? ---> 5 || Porque la primera e que aparece está en el índice 5 de la cadena

#! IMPORTANTE!!!!
#? No todo en las cadenas funciona como en las listas, por ejemplo, a las cadenas no se le puede aplicar 
#? los métodos que se le aplican a las listas, como el append, insert, extend, etc, pero sí se puede crear
#? una copia de la cadena concatenándole lo que le quiera agregar. 

# alphabet = "bcdefghijklmnopqrstuvwxy"       #? Se crea el alfabeto sin la a ni la z

# alphabet = "a" + alphabet                   #? Aquí se añade la a, sumándola antes del alfabeto. 
# alphabet = alphabet + "z"                   #? Aquí se añade la z, sumándola después del alfabeto. 

# print(f"{alphabet}")                        #? ---> abcdefghijklmnopqrstuvwxyz