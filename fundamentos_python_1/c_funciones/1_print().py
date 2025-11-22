
#!             _____  _    _  _    _   _____  __   ___   _    _     _____   _____   __  _   _  _______  
#!            |  ___|| |  | || \  | | / ____||  | / _ \ | \  | |   |  __ \ |  __ \ |  || \ | ||__   __|
#!            | |__  | |  | ||  \ | || |     |  || | | ||  \ | |   | |__) || |__) ||  ||  \| |   | |   
#!            |  __| | |  | ||   \| || |     |  || | | ||   \| |   |  ___/ |  _  / |  || . ` |   | |   
#!            | |    | |__| || |\   || |____ |  || |_| || |\   |   | |     | | \ \ |  || |\  |   | |   
#!            |_|     \____/ |_| \__| \_____||__| \___/ |_| \__|   |_|     |_|  \_\|__||_| \_|   |_|   


#? Print() es una función en python como cualquier otra y su función es mostrar en la consola lo que quiero que muestre

#TODO: Mostrando variables

#?          Puede mostrar variables, las cuales tienen un valor, en ese caso no se muestra el nombre de la variable, sino,
#?          lo que está guardado en la variable, así:
#           a = 20
#           print(a) ---> 20

#TODO: Mostrando mensajes

#?          También se puede mostrar un simple texto, el cual debe ir entre comillas, así:
#           print("Este es un simple mensaje") ---> Este es un simple mensaje

#TODO: Haciendo operaciones dentro del print. 

#?          Puedo hacer operaciones dentro de un print y el resultado se mostrará en pantalla, ejemplo:

#           print(20 + 50) ---> 70 #? Toma los números dados y los opera según el operador lógico dado
#           print(2 ** 2) ---> 4 #? Esto eleva el primer 2 a la 2
#           a = 20
#           print(a * 2) ---> 40 #? Como a es igual a 20, al multiplicarse por 2, es igual a 40


#TODO: Mensajes + variables

#?      También es posible mezclar solo mensajes con variables dentor del print, para ello hay dos formas:

#           TODO:  1 Forma: 
#?          Dentro del print, se concatenan los mensajes con las variables, usando una coma luego de cada mensaje o
#?          variable y el símbolo +, así:
#           a = 20
#           b = 40
#           print("La multiplicación de", a, "X", b, "Es igual a", a*b) ---> La multiplicación de 20 X 40 Es igual a 800

#           TODO:  2 Forma:
#?          Dentro del print se pone inicialmente una f y luego todo se pone en comillas, pero cada variable u operación
#?          entre variables se pone entre llaves regulaes, Así:
#           a = 20
#           b = 40
#           print(f"La multiplicación de{a} X {b} Es igual a {a*b}") ---> La multiplicación de 20 X 40 Es igual a 800
#?          De este manera nos ahorramos el poner comas, que aunque funcionales, pueden ser confusos.


#TODO:      Comillas dentro del print:
#?          Cuando necesito poner comillas dobles dentro de un string que ya de por sí va con comillas dobles, se
#?          generaría una confusión entre las comillas, pero puedo darle escape a mis comillas dentro del string 
#?          agregando un backslash antes de cada comilla, así:
#           print(f"Este es mi texto con \"comillas dobles\"") #? 

#TODO:              Comillas simples fuera o dentro del string
#?                  Para no tener que hacer el backslash, puedo usar comillas simples para todo el String y 
#?                  comillas dobles para la palabra o frase interna que quiero resaltar o visebersa, así:
#                   print(f"Este es mi texto con 'comillas simples'") 
#                   print(f'Este es mi texto con "comillas dobles"')



#! OJOO IMPORTANTE: Python tiene 2 argumentos que modifican su comportamiento
# !solo funcionan cuando se ponen al final de los demás argumentos. 
         
#TODO:      Argumento finalizador end
#?          Los print siempre hacen un salto de línea luego de su ejecución, por lo que un próximo print lo que hace
#?          es ejecutarse en el renglón de abajo, pero eso es editable usando la palabra clabe end, así:
#           print(f"Mañana vamos a jugar con", end =" ") #! 1er print 
#           print(f"Miguel") #! 2do print
#           Resultado por consola: Mañana vamos a jugar con Miguel
#!                                         1er print     2do print  

#TODO:      Argumento separador sep
#?          También es posible usar separadores generales de cada palabra en el print, para lo que se usa la palabra
#?          clave sep, que sirve para serarar cada String (Cada sentencia que vaya entre comillas)
#           print(f"Mañana", "vamos", "a", "jugar", "con", "Miguel", sep = "***") --> Mañana***vamos***a***5***jugar***con***Miguel


#TODO:      MEZCLANDO TODO LO APRENDIDO AQUI

#           a = 2 
#           b = "El mejor"
#           print("Mi nombre es 'Carlos', " * a, f"\"Castaño\"" {b}",  sep = "*** ", end=" - ")
#?            Imprime minombre es 'Carlos'    | Imprime Castaño con |tras cada string | Finaliza con un -
#?                  y lo multiplica           | comillas y trae     |separa con ***   | en lugar de 
#?                  por a que es 2            | b que es "Elmejor"  |al siguiente     | saltar línea
#           print(f"Rodríguez") #? No queda en el renglón de abajo porque el print anterior termina con -, 
#?                                 no salto de línea

#           Resultado: Mi nombre es Carlos, Mi nombre es 'Carlos', *** "Castaño" El mejor - Rodríguez











a = 2 
b = "El mejor"
print("Mi nombre es 'Carlos', " * a, f"\"Castaño\" {b}",  sep = "*** ", end=" - ")
print(f"Rodríguez")
