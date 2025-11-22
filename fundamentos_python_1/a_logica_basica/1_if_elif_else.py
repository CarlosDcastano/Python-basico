
#!                  __    _____          _____   _       __    _____         _____   _       _____   _____ 
#!                 |  |  |  ___|        |  ___| | |     |  |  |  ___|       |  ___| | |     |  ___| |  ___| 
#!                 |  |  | |__          | |___  | |     |  |  | |__         | |___  | |     | |___  | |___ 
#!                 |  |  |  __|         |  ___| | |     |  |  |  __|        |  ___| | |     | __  | |  ___|
#!                 |  |  | |            | |___  | |___  |  |  | |           | |___  | |___   ___| | | |___ 
#!                 |__|  |_|    _       |_____| |_____| |__|  |_|   _       |_____| |_____| |_____| |_____|
#!                             | |                                 | |   
#!                             |/                                  |/ 

#? Cuando tengo una difurcación en mi código, es decir, las acciones que continúan en mi código dependen de un resultado
#? debo usar la sentencia if, por ejemplo, pongo una condición, si la condición se cumple, hago algo, si no se cumple
#? hago algo diferente. 

#TODO: Ejemplo de la vida real. 
#?          si hace buen tiempo:
#?              saldremos a caminar

# weather_is_good = True
# if weather_is_good: #? Aquí se da la condición, terminando con dos puntos
#     print("go_for_a_walk") #? Aquí se dice lo que se hará si la condición se cumple. 

#TODO:      Ejemplo práctico:
#?               Queremos validar si un usuario ingresa el correo correcto guardado en una base de datos

# usuario = "carlosmau@hotmail.com" #? Se creó un usuario manualmente y se guarda en la base de datos
# ingreso = input("Por favor ingrese el usuario")) #? Se pide al cliente ingresar el usuario

# if ingreso == usuario: #? Aquí se da una condición, si el cliente ingresó el mismo correo que hay en usuario
#     print("Acceso concedido") #? Si es verdadero, es decir, sí es el mismo usuario, se muestra el mensaje


#! Qué pasa cuando no se cumple la condición? 

#?          Si lo dejamos así, solo con el if, el código no haría nada, para que haga algo acuando la condición
#?          no se cumple, debemos poner la palabra else o elif, cuando tenemos más de una condición por evaluar,
#TODO:      Ejemplo práctico:
#?              Ahora nuestro cliente debe escribir tanto el usuario como la contraseña y debe validarse 
#?              si tiene acceso o no, si son correctos ambos datos, debe mostrar Acceso concedido, si el usuario es 
#?              incorrecto debe mostrar, usuario no existe. Si el usuario es correcto, 
#?              pero la contraseña incorrecta, debe mostrar "COntraseña incorrecta"

#                           !!!!! Código !!!!!! 
# while True:
#     usuarios_db = {                         #? 
#     "miguel@gmail.com":"contraseña1",       #? SIMULANDO UNA
#     "carlosmau@hotmail.com": "contraseña2", #? BASE DE DATOS
#     "oscarfi@gmail.com": "contraseña3"      #? CON UN 
#     }                                       #? DICCIONARIO

#     usuario = input("Por favor ingrese su usuario: ") #? El cliente ingresa su usuario
#     contra = input("Por favor ingrese su contraseña: ") #? El cliente ingresa su contraseñ

#     if usuario in usuarios_db: #? Si el usuario ingresado está en el diccionario
#         if usuarios_db[usuario] == contra: #? Si el usuario que sí está, ingresó la contraseña correcta
#             print("Acceso concedido") #? Dile, acceso concedido
#         else:  #? Si el usuario que sí está no ingresa contraseña correcta
#             print("Contraseña incorrecta") #? Dile, contraseña incorrecta
#     else:       #? Si el usuario ingresado no está en el diccionario (Base de datos)
#         print("Usuario no registrado")  #? Dile,  usuario no registrado. 

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#TODO: Datos claves:

#TODO: Cuando usar elif
#?          Cuando tengo más de una condición por evaluar, debo usar elif, ejemplo: Si tengo un escenario en el que 
#?          tengo varios caminos a seguir, dependiendo de lo que el usuario haga. 
#TODO:              Ejemplo práctico:
#?                      Una discoteca solo permite ingresar mayores de 18 años o menores acompañados por un mayor

#                               !!!!!!Código!!!!!

# edad = int(input("Ingrese su edad"))
# edad_com = int(input("Ingrese edad del acompañante"))

# if edad >= 18:
#     print(f"Puede ingresar")

# elif edad < 18 and edad_com >= 18:
#         print(f"Pueden ingresar")
        
# else:
#     print(f"No puede ingresar")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!

