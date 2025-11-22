
#!                              __          __  _    _  __  _      _____ 
#!                             |  |        |  || |  | ||  || |    |  ___|
#!                             \  \        /  /| |__| ||  || |    | |___ 
#!                              \  \  /\  /  / |  __  ||  || |    |  ___|
#!                               \  \/  \/  /  | |  | ||  || |___ | |___ 
#!                                \___/\___/   |_|  |_||__||_____||_____|


#! DEFINICIÓN BÁSICA DEL CICLO WHILE 
#? Un ciclo while en Python se utiliza para ejecutar repetidamente un bloque de código mientras una condición 
#? sea verdadera. Se evalúa la condición antes de cada iteración, y el ciclo se detiene cuando 
#? la condición se vuelve falsa.

#! IMPORTANTE: 
#? No solo cuando la condición se vuelve falsa es que se rompe el ciclo, también cuando añado un break, es decir
#? cuando le doy una condición de rompimiento al ciclo, also como, si la condición no se ha cumplido, pero 
#? pasa tal cosa, rómpete y termina el ciclo. 

#! SINTAXIS!!!

# while condicion:
    # Bloque de código a ejecutar
    
#TODO: EJEMPLO BÁSICO:

# contador = 1          #?Creo una variable llamada contador y la inicializo en 1
# while contador <= 5:  #? Establezco la condición de que mientras el contador sea menor o igual a 5
#     print(contador)   #? Muéstrame el contador
#     contador += 1     #? Incrementar el contador en cada iteración de uno en uno para que pueda llegar a ser 5
#                       #?-- y así llegar al fin del ciclo, si no lo hago, el ciclo sería infinito. 

#TODO: EJEMPLO CON UN IF:
# counter = 0                   #? Creo una variable counter y la inicializo en 0
# while counter <11:            #? Doy una condición de que se haga lo de adentro mientras el contador sea menor a 11
#     if counter % 2 != 0:      #? Creo una condición interna, si el counter no es par
#         print(f"{counter}")   #? Muéstralo en la pantalla (De modo que no se muestran los números pares)
#     counter += 1              #? Incrementar el contador en cada iteración de uno en uno para que pueda llegar a ser 5
#                               #?-- y así llegar al fin del ciclo, si no lo hago, el ciclo sería infinito.

#TODO USO DE ELSE CON WHILE
                        #? Cuando un ciclo finaliza, tengo la opción de poner un mensaje de salida, indicando
                        #? que el ciclo ha culminado porque ya no se cumple la condición, como a continuación:
                        
n = 3                   #? Creo una variable y le asigno el valor de 3

while n > 0:            #? Mientras se cupla la condición de que n sea mayor a 0 
    print(n + 1)        #? Si eso se cumple, realiza esto de mostrar n + 1, es decir, haz la suma y muestra el resultado
    n -= 1              #? Ahora a n se le asignará lo que hay en n menos 1, para que el ciclo se rompa en algún momento
else:                   #!Esto es lo diferente ahora, si detallamos, el ciclo while es casi un if pero en ciclos, por eso, cuando ya no se cumple la fucondición, puedo poner un else
    print("Ya no se cumple la función, ya se llegó a ", n)  #! En ese else, puedo poner un mensaje informando que el ciclo ya se rompió porque no se cumple la condición

#TODO: Otro ejemplo de while usando else cuando el ciclo finaliza

# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("Ya se llegó a:", i, "ese número no hace parte de la lista válida") #! El uso de else aquí, es para decir
         #!que la condición ya no se cumple, por lo que el bucle finaliza. 