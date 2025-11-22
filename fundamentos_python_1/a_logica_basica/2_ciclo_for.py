
#!                                               _____   ___   _____  
#!                                              |  ___| / _ \ |  __ \ 
#!                                              | |__  | | | || |__) |
#!                                              |  __| | | | ||  _  / 
#!                                              | |    | |_| || | \ \ 
#!                                              |_|     \___/ |_|  \_\



#? Los ciclos for se usan para recorrer o iterar una secuencia de elementos como una lista, un diccionario,
#? Una tupla, un conjunto o un rango determinado de números
#? OJO!!! Al ser un ciclo, no solo se usa para recorrer listas, sino que puedo hacer que con cada recorrido
#? haga algo repetidamente, por ejemplo, si quiero que la tabla del 1 al 12 sea mostrada, puedo usar ciclos
#? Si quiero llenar una lista de valores, también puedo usar ciclos. 

#!SINTAXIS!

# for i in "iterable":
#     Código, if, funciones, prints, demás.....  

#                     #? La palabra reservada for indica el inicio del ciclo, i, es el índice que recorrerá
#                     #? el iterable indicado para el ciclo, ese iterable puede ser una lista existente, tupla
#                     #? conjunto, diccionario, o un rango que yo manualmente quiera darle, finalizando con :
#                     #? Al dar enter, VSC deja el renglón y hace la indentación correspondiente, allí, dentro
#                     #? del ciclo es donde escribimo qué es lo que queremos hacer por cada vez que el ciclo
#                     #? de la vuelta. 

#TODO: Ejemplo sencillo, mostrando los números en el rango del 1 al 10

# for i in range(1,11): #?Los números dentro del paréntesis determinan el inicio y el fin del rango, el límite 11, no se toma, es decir, que llega hasta el 10
#     print(f"{i}") 
#                    #? i toma el valor de 1 e ingresa al código, entonces nuestro código lo que hace es mostrar
#                    #? i, y si i vale 1, muestra 1, sale de allí y ahora i toma el valor siguiente, que es 2,
#                    #? ingresa al código valiendo 2 y muestra i que hora vale 2, y así hasta terminar el ciclo en
#                    #? el número 10, mostrando i que finalmente será el 10, vuelve al for a continuar, pero se
#                    #? da cuenta que no tiene más números por recorrer, entonces finaliza el ciclo. 

#TODO: Ejemplo sencillo mostrando los números en el rango del 0 al 20 condicionando el incremento

#? De forma automática, python está creado para que dentro de un rango, al terminar el primer recorrido, i se
#? incremente en una unidad, pasando lógicamente de 1 a 2 y luego a 3, después a 4 y así hasta finalizar, pero,
#? esto puede cambiar cuando al rango, le damos un tercer argumento, ese tercer argumento determina de cuanto en
#? cuanto incrementa i. 

# for i in range(0,22,3): #?El recorrido empieza desde el cero, hasta el 21 saltando de a 3, i valdra 0 y luego 3 
#     print(f"{i}") #?Mostrará los números 0 3 6 9 12 15 18 21

#TODO: Ejemplo práctico sobre la tabla del 1 al 12 con ciclo for

# for i in range(1,13): #?Creo mi ciclo para recorrer los números del 1 al 12
#     print(f"\nEsta es la tabla del {i}") #?Por cada recorrido, muesrtra este mensaje
#     for j in range(1,13): #? Por cada recorrido va a hacer un ciclo interno, también del 1 al 12
#         print(f"{i} X {j} = {i*j}") #? En ese recorrido interno es donde va a mostrar la multiplicación de j por i

                                    #!Explicación: En el ciclo externo, se recorre el rango de 1 a 12, pero cada
                                    #! recorrido, es decir, cuando i vale 1, ingresa al ciclo interno, y empieza
                                    #! a recorrer el ciclo del 1 al 12, donde j vale 1, por ello, en ese print 
                                    #! interno, se expone i*j, como ambos valen 1, sería 1*1 = 1, ahí termina el
                                    #! primer recorrido de j, el cual vuelve a iniciar, pero ahora valiendo 2,
                                    #! entonces la siguiente expresión i*j, sería 1*2 = 2, termina el segundo 
                                    #! recorrido y sigue así hasta llegar a cuando i*j sería igual a 1*12= 12
                                    #! En ese momento, termina todo ese ciclo y sale de allí al ciclo externo,
                                    #! donde el valor de i ya no es 1, sino que empieza a valer 2 e ingresa de nuevo
                                    #! al ciclo interno, donde hace todo el mismo recorrido anteriormente del 1 al 12
                                    #! pero esta vez i valiendo 2, todas las tablas serían con el 2. 


#! |||||||||||||||||||||||||||||||||||||||||||||||||||
#TODO: PALABRAS CLAVE BREAK Y CONTINUE
#!||||||||||||||||||||||||||||||||||||||||||||||||||||

#? Puede haber un momento en el que deseo que mi código en un ciclo, cuando se cumpla alguna condición
#? el código pare o la ignore, para eso, existen las sentencias break (Detenerse) y continue (Ignora y sigue)

#TODO: EJEMPLO DE CÓMO USAR BREAK
                    #? Queremos un código que se dedique a leer un correo, muestre lo que hay antes de 
                    #? dicho arroba solamente, es decir, cuando llegue al @ se rompa el ciclo y se detenga

# for ch in "john.smith@pythoninstitute.org":  #? Por cada caracter en "el correo dado"
#     if ch == "@":                            #? Si el caracter es @
#         break                                #? Deja de ejecutarte
#     print(ch, end="")                        #? A medida que se ejecuta, agrega ese CH al print y finaliza con 
#                                            #? ningún espacio para que la siguiente letra quede pegada

#TODO: EJEMPLO DE CÓMO USAR BREAK
                    #? Queremos un código que se dedique a leer una cadena de dígitos, y muestre los dígitos
                    #? pero, ignorando el cero y además, en lugar de cero, escriba una x

# for digit in "0165031806510":              #? Por cada dígito en "la cadena de dígitos dados"
#     if digit == "0":                       #? Si uno de esos dígitos es igual a 0
#         print("x", end="")                 #? Escriba X sin dejar renglón
#         continue                           #? Ignora el cero y sigue con lo demás
#     print(digit, end="")                   #? Al seguir escriba el dígito leído y no dejes renglón



#TODO: EJEMPLO ADICIONAL DE CONTINUE 

# frase = input("Ingrese una frase ")  #?Le pido al usuario ingresar una frase que se guardará en la variable frase
# frase = frase.upper()                #? Combierto la frase a mayúscula con el método de objetos String .upper()
# frase_sin_vocales = ""               #? Creo la variable frase_sin_vocales, vacía que usaré más adelante

# for ch in frase:                     #? Creo el ciclo for, por cada caracter en la frase
#     if ch in "AEIOU ":               #? si ese caracter es una vocal, es decir, si el caracter está en "AEIOU"
#         continue                     #? Se es así, ignóralo y continua con el siguiente caracter
#     frase_sin_vocales += ch          #? Agrega el caracter a la variable frase_sin_vocales

# print(f"{frase_sin_vocales}")        #? Muestra lo que ya hay en la variable frase_sin_vocales


#! LLENANDO LISTAS CON FOR
                    #? En efecto, uno de los usos básicos de for es para llenar listas como se hará a continuación:

# lista = []           #?Creo una lista vacía
# for i in range(15):  #?Creo el ciclo for con el rango hasta donde quiero llenar mi lista
#     lista.append(i)  #? por cada vuelta al ciclo agrégame i a mi lista, así, el primer i será 0, sel segundo 1, y así
#     print(lista)     #? Muéstrame la lista cada vez que haga un ciclo para ver cómo va creciento, (OPCIONAL)
# #                    #? Al final, la lista será: --->[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#TODO: Ejemplo de llenado de listas con for, usando continue y break

lista = []               #?Creo una lista vacía

# for i in range(15):      #?Creo el ciclo for con el rango hasta donde quiero llenar mi lista
#     if i >=11:           #? si el número es mayor o igual a 11 
#         break            #? Si es así, rompe el ciclo, detente!
#     if i % 2 ==0:        #? Si i es par 
#         continue         #? Ignóralo y contiinúa con el siguiente
#     lista.append(i)      #? Agrega el número a la lista (Solo impares porque los pares están siendo ignorados)

# print(f"{lista}")        #? Al final, la lista será: --->[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]




# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")
    
# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")
    


#!Ojo aquí con el uso del continue, cuando quiero que se ignore el resultado de una lectura y siga con lo demás. 

# frase = input("Ingrese una frase ")
# frase = frase.upper()
# frase_sin_vocales = ""

# for ch in frase:
#     if ch in "AEIOU ":
#         continue
#     frase_sin_vocales += ch

# print(f"{frase_sin_vocales}")


