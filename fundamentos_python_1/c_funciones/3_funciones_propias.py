
#! _____  _    _  _    _   _____  __   ___   _    _  _____  _____     _____   _____    ___   _____   __      __      _____ 
#!|  ___|| |  | || \  | | / ____||  | / _ \ | \  | ||  ___||  ___|   |  __ \ |  __ \  / _ \ |  __ \ |  |    /  \    |  ___|
#!| |__  | |  | ||  \ | || |     |  || | | ||  \ | || |___ | |___    | |__) || |__) || | | || |__) ||  |   / /\ \   | |___ 
#!|  __| | |  | ||   \| || |     |  || | | ||   \| ||  ___|| __  |   |  ___/ |  _  / | | | ||  ___/ |  |  / ____ \  | __  |
#!| |    | |__| || |\   || |____ |  || |_| || |\   || |___  ___| |   | |     | | \ \ | |_| || |     |  | / /    \ \  ___| |
#!|_|     \____/ |_| \__| \_____||__| \___/ |_| \__||_____||_____|   |_|     |_|  \_\ \___/ |_|     |__|/_/      \_\|_____| 

#? Cuando estamos programando, se hace necesario volver a usar un código que ya usé previamente;
#? lo que se hacía antes era copiar y pegar dicho código, lo cual, no solo era engorroso, sino,
#? que también hacía el código muy largo, para eso, se usan las funciones, que son:
#? Código encapsulado, el cual una vez creado, puedo llamarlo simplemente por su nombre para,
#? traérmelo de donde sea que esté y usarlo en ese punto de mi código donde lo necesito. 

#TODO: SINTAXIS

#? SOlo debo usar la palabra reservada def, seguida del nombre que quiero darle a mi función,
#? luego un par de paréntesis y finalizo con dos puntos, en el siguiente renglón, ya indentado
#? lo que hago es escribir lo que quiero que haga mi función; así:

# def mi_función():
#     print("Yo soy una función básica")

#!|||||||||||||||||||||||||||||||Pero luego cómo la uso? 

#? Solo se debe llamar usando su nombre y los paréntesis, así. 

#TODO: Ejemplo práctico

# def mi_función():   #?Creo la función como ya se enseñó
#     print("Yo soy una función básica") #? Aquí va lo que quiero que haga mi función

# #? Todo 
# #? Aquí
# #? Es
# #? Simulación
# #? De
# #? Cientos
# #? De
# #? Líneas
# #? De
# #? Código

# mi_función() #? Aquí después de cientos de línas de código, llamo mi_función 
#              #? Resultado: LA CONSOLA MOSTRARÁ: Yo soy una función básica

#!||||||||||||||||||||||||||||||||||||||||

#TODO: FUNCIONES CON PARÁMETROS, LLAMANDO CON ARGUMENTOS:

#! Ojo aquí!!!!!   Parámetros es lo que pongo en el paréntesis al momento de crear la función
#! Ojo aquí!!!!!   Argumentos es lo que pongo en el paréntesis al momento de llamar a la función

#? Hay momentos en los que nuestra función va a requerir de ciertas condiciones para funcionar, o ciertos
#? parámetros con los cuales trabajaría, esos parámetros son los que van dentro del paréntesis. 

# def saludar(x): #? En este caso, tengo un parámetro el cual es X, quiere decir que si invoco mi función, debo incluírle un argumento por X
#     print(f"Hola!,{x} ¿Cómo estás?")

# #? TODO 
# #? Aquí
# #? Es
# #? Simulación
# #? De
# #? Código

# nombre = input("Por favor ingrese su nombre")
# print(f"{saludar(nombre)}") #? EL argumento que le estoy pasando es la variable nombre

#TODO: PARÁMETROS POR ORDEN: 

#? El orden de los parámetros determina igualmente en qué orden se reciben los argumentos, ejemplo:

# def sumar(a,b):
#     print(a+b)

# #? TODO 
# #? Aquí
# #? Es
# #? Simulación
# #? De
# #? Código

# sumar(8,5) #? EL argumento 8 toma el lugar del parámetro a y 5 el lugar de b; el resultado es 13
#!          Ojoooo, en este caso, se sabe que 8 toma el lugar de a y 5 el lugar de b de manera automática

#TODO: ALTERANDO EL ORDEN DE LOS ARGUMENTOS SIN AFECTAR EL ORDEN DADO EN LA FUNCIÓN:

#?  En el siguiente ejemplo, vemos cómo al llamar la función saludo, los argumentos se pasan en orden diferente
#? escribiendo el nombre de los parámetros igual a mi argumento, pero esto no afecta el orden dado
#? en el cuerpo de la función

# def saludo(first_name, last_name): #?PArámetros en order (first_name, last_name)
#     print("Hello, my name is", first_name, last_name) #? Aquí es donde se define el orden en que quiero que aparezcan

# #? TODO 
# #? Aquí
# #? Es
# #? Simulación
# #? De
# #? Código

# saludo(last_name = "Skywalker", first_name = "Luke") #? PEro al llamarlo, lo llamo en otro orden, sin afectar el
#                                                      #? cuerpo de la función.

#! NOTA IMPORTANTE:

#? Al invocar una función, al momento de ingresar los argumentos, puedo ingresarlos por orden posicional o con su
#? nombrre de parámetro, por ejemplo:

#TODO: Por orden posicional:

# def sumar(a,b,c):
#     print(a, "+", b, "+", c, "=", a + b + c)

# #? TODO 
# #? Aquí
# #? Es
# #? Simulación
# #? De
# #? Código
  
# sumar(1,2,3) #? Aquí de forma posicional, 1 es a, 2 es b y 3 es c ---> 1+2+3 = 6

#TODO: Por palabra clave; usando el nombre del parámetro
# def sumar(a,b,c):
#     print(a, "+", b, "+", c, "=", a + b + c)

# #? TODO 
# #? Aquí
# #? Es
# #? Simulación
# #? De
# #? Código

# sumar(c=1, b=3, a=2) #? Aquí por palabra clave, usando el nombre del parámetro ---> 2+3+1 = 6

#TODO: Mezclando por orden posicional y con palabra clave, usando el nombre del parámetro.

# def sumar(a,b,c):
#     print(a, "+", b, "+", c, "=", a + b + c)

# #? TODO 
# #? Aquí
# #? Es
# #? Simulación
# #? De
# #? Código

# sumar(1, b=2, c=3) #? EL 1 se ingresa de forma posicional representando la a, y b y c se ingresa con el nomre del parametro

#! OJoooooo. No se puede poner un argumento con palabra clave (Usando el nombre del parámetro) y luego de este
#! un argumento sin palabra clave, solo por orden, eso causa un error de interpretación.

#TODO: Ejemplo del error:

# def sumar(a,b,c):
#     print(a, "+", b, "+", c, "=", a + b + c)

# #? TODO 
# #? Aquí
# #? Es
# #? Simulación
# #? De
# #? Código

# sumar(a=1, 2, c=3) #? EL número 2, que es el argumento b, aunque está en la posición correcta, antes de él 
#                    #? hubo un argumento establecido por palabra clave, por lo que marcará error.


#!|||||||||||||||||||||||||||||||||||||||||

#TODO: PARÁMETROS DEFINIDOS POR DEFECTO:

#? HAy momentos en los que puedo darle valor por defecto a mi parámetro al momento de crear la función, de modo que
#? si no tengo alguno de los argumentos, sea automáticamente dado por el valor que tiene el parámetro asignado, así:

#TODO: Ejemplo práctico:

# def saludo(name="lucas", lastname="Castaño"): #? En los parámetros, directamente le doy un valor por defecto
#     print(f"Hola, mi nombre es {name} {lastname} ")

# #? TODO 
# #? Aquí
# #? Es
# #? Simulación
# #? De
# #? Código

# saludo() #? Aquí no puse ningún argumento, pero el resultado es ---> Hola, mi nombre es lucas Castaño
#          #? Ya que aunque no le pasé argumentos, ya los mismos fueron definidos en la creación de la función
#          #? Si sí le paso argumentos, se ignoran los parámetros por defecto y se tienen en cuenta los 
#          #? argumentos que le paso al momento de invocar la función. 

#!||||||||||||||||||||||||||||||||||||||||||||||

#TODO: RETORNO DE UNA FUNCIÓN:

#? Las funciones que hemos visto solamente muestran un mensaje por consola, osea, la lógica se realiza toda
#? dentro de un print, por lo que no puedo usar esa función dentro de una función, o aplicarle más procesos
#? cuando la invoque, ya que no se pueden hacer mayor cosa con un print. 

#! Entonces cuál es la solución?????????????

#TODO: RETURN

#? Es una palabra clave para indicar que lo que hace mi función puede almacenarse en una variable para su uso
#? posterior, no dentro de un print, sino directamente en una variable. Así:

#TODO: Ejemplo práctico:

            #TODO Ejemplo con solo print:

# def sumar(a,b):
#     print(f"El resultado de sumar {a} + {b} es {a+b}")


# #? TODO 
# #? Aquí
# #? Es
# #? Simulación
# #? De
# #? Código

# numero1 = 5
# numero2 = 6

# resultado = resultado = sumar(numero1, numero2) /2 #? Si hago esto, dará error, porque al no haber return, 
#                                 #? el tipo de resultado que retorna es None y None no se puede opear como un entero. 

# print(resultado) #? No hay resultado por mostrar porque no hay un return. 


            #TODO: Ejemplo usando return

# def sumar(a,b):
#     return a+b  #? En lugar de un print, le doy un return que puede usarse para aplicarle más lógica

# #? TODO 
# #? Aquí
# #? Es
# #? Simulación
# #? De
# #? Código

# numero1 = 5
# numero2 = 6
# resultado = sumar(numero1, numero2)

# print(resultado/2) #? El resultado que es 11, se divide entre 2, sin error, ya que mi return, no es None, sino
                        #? un entero. 
                        
#!||||||||||||||||||||||||||||||       
#TODO: EL ALCANCE

#? Hace referencia a qué alcance tiene un elemento (variable, iterable, u otro) dentro o fuera de una función
#!NOTA IMPORTANTE: Recordemos que una función es código empaquetado, hermétivo hasta que se le invoca. 
#? Al ser hermético, las variables o listas que se creen en ella, solo existen para sí, no tienen un alcance
#? gloval, pero, sí reconoce variables que vengan de afuera de ella, es decir del resto del código. 

#TODO: Ejemplo práctico

# def sumar(a,b):
#     resultado = a+b

# sumar(5,6)
# print(resultado) #? Esto marca un error porque la variable resultado se está llamando desde el código global
#                  #? Pero esa variable fue creada dentro de una función, por lo que no se reconoce afuera. 
#                 
# 

#? LA forma de darle salida sin invocar la función es asignándole un tipo de dato global. 


#!Así:

# def sumar(a,b):
#     global resultado #? Primero se escribe la palabra reservada global, seguida por el nombre de la variable
#     resultado = 8    #? Luego se le asigna un valor a la variable (No se puede asignar en la misma línea del global)
#     return resultado

# sumar(5,6)     #! Ojo!!! SOlo se reconocen las variables cuando hago invocación de la función, recordar que  crear una función es hermética, nada entra ni sale hasta que la invoque. 
# print(resultado)

#TODO: CONTENIDO DENTRO DE LAS FUNCIONES:

#? Dentro de las funciones no solo se procesan textos o funciones matemáticas, sino que puede existir toda una
#? lógica de código que entrará en acción cuando invoque la función, por ejemplo, puede que todo lo que
#? haya dentro de la función transacción() tenga todo lo necesario para realizar una transacción bancaria, entre
#? pedir datos al usuario, cantidad de dinero, hacia dónde va el dinero, si se trata de retirar, y demás. Esto
#? implica que hayan muchas líneas de código dentro de esa función, las cuales, de hecho pueden invocar otras
#? funciones dentro de ella, dándole argumentos para que toda la función transacción en sí, funcione. 

#! EL SIGUIENTE ES UN EJEMPLO DE UNA CALCULADORA USANDO FUNCIONES DENTRO DE FUNCIONES:

# """Calculadora"""
def sumar (a,b):         #? Creando la función sumar
    return a + b

def restar (a,b):        #? Creando la función restar 
    return a - b

def multiplicar (a,b):   #? Creando la función multiplicar
    return a * b

def dividir (a,b):       #? Creando la función dividir
    if b != 0:           #! Dándole lógica extra a mi función con un if
        return a /b      #! Retorna la división si se cumple el if
    else:
        return "Error, no es posible dividir entre cero"  #! Si no se cumple la condición, retorna un mensaje

def deifinir_operaciones ():  #? Creando la función en la que por medio de un diccionario se definen las operaciones
    return {
        1: sumar,
        2: restar,        #? Aquí se puede detallar el diccionario con sus claves y el valor correspondiente
        3: multiplicar,
        4: dividir
    }

def opciones ():   #? Creando la función del menú de opciones que solo muestra por consola al usuario las opciones a seleccionar en la calculadora
    print("MENÚ DE OPERACIONES")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def ejecutar ():   #? Creando la función ejecutar que es la principal y acoje las demás funciones
    while True:   #? Ciclo infinito para que se repita siempre hasta que llegue a un break. 
        opciones()  #? Invoco la función opciones para mostrarlas al usuario
        try:
            opcion = int(input("Por favor ingrese el número correspondiente a la operación que desea realizar: "))
        except ValueError:
            print("El número debe ser un número entero y debe estar dentro de la lista dada")
            continue
        
        if opcion == 5:  #? Si la oopción que el usuario ingresa es 5, se acciona el break y sale del ciclo while
            print("Adios")
            break
        
        operaciones = deifinir_operaciones() #? Asigno el return de la función definir_operaciones() a la variable
                                             #? operaciones
        if opcion in operaciones:    #? Si la opción que el usuario ingresó está dentro de las claves del diccionario que retorna definir_operaciones()
            try:
                a = int(input("Por favor ingrese el primer número entero: "))
                b = int(input("Por favor ingrese el segundo número entero: "))
            except ValueError:
                print("Debe ingresar un número entero")
                continue
        
            resultado = operaciones[opcion](a,b) #? A la variable resultado, le asigno lo que hay en operaciones
                                                 #? El cual tiene asignado el diccionario clave valor.
                                                 #? Si el usuario ingresa una opción dentro de las dadas
                                                 #? se toma el valor de esa opción en el diccionario y se le pasan
                                                 #? los parámetros (a,b)
        
            print(f"El resultado es {resultado}")  #? Aquí se muestra por consola la variable resultado
        
        else:
            print("El valor es debe estar dentro de las opciones dadas") #? Si la opción que el usuario ingresa
                                                                         #? no está dentro del diccionario
                                                                         #? se arroja este menaje y se repite el ciclo
        

ejecutar() #? Aquí se invoca la función que contiene toda la ejecución y solo así se ejecuta el código, si no la
           #? invocara nunca dentro de mi código, la misma nunca va a funcionar 
           #!DEBO DE INVOCARLA SIEMPRE QUE QUIERA QUE ELLA O UNA DE SUS VARIABLES O CICLOS INTERNOS APAREZCA