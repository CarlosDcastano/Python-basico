
#! _____  _    _  _    _   _____  __   ___   _    _  _____  _____     __  __  __  _____    ___   _____   _______      __      ____       __      _____ 
#!|  ___|| |  | || \  | | / ____||  | / _ \ | \  | ||  ___||  ___|   |  ||  \/  ||  __ \  / _ \ |  __ \ |__   __|    /  \    |  _ \     /  \    |  ___|
#!| |__  | |  | ||  \ | || |     |  || | | ||  \ | || |___ | |___    |  ||      || |__) || | | || |__) |   | |      / /\ \   | | | |   / /\ \   | |___ 
#!|  __| | |  | ||   \| || |     |  || | | ||   \| ||  ___|| __  |   |  || |\/| ||  ___/ | | | ||  _  /    | |     / ____ \  | | | |  / ____ \  | __  |
#!| |    | |__| || |\   || |____ |  || |_| || |\   || |___  ___| |   |  || |  | || |     | |_| || | \ \    | |    / /    \ \ | |_| | / /    \ \  ___| |
#!|_|     \____/ |_| \__| \_____||__| \___/ |_| \__||_____||_____|   |__||_|  |_||_|      \___/ |_|  \_\   |_|   /_/      \_\|____/ /_/      \_\|_____|

"""Este archivo solo será explicativo, por lo que no habrá ejemplos, para ejemplos debemos seguir la carpeta
2_fundamentos_python en el archivo modulos.py"""

#! ¿Por qué hay funciones que se tienen qué importar y no hacen parte del lenguaje directamente en python?

#? En Python, algunas funciones no están incluidas directamente en el lenguaje base porque Python sigue el principio 
#? de diseño conocido como "baterías incluidas" (batteries included), pero también prioriza la simplicidad y 
#? modularidad.Esto significa que ofrece una amplia gama de funcionalidades, pero organiza muchas de ellas en 
#? módulos especializados.A continuación, te explico las razones principales por las que algunas funciones necesitan importarse:



#TODO: 1. Mantener la simplicidad del lenguaje base

#? - El núcleo de Python está diseñado para ser ligero, fácil de aprender y usar, especialmente para principiantes.

#? - Incluir demasiadas funcionalidades directamente en el lenguaje base lo haría más complejo y menos manejable.

#? - Funciones avanzadas o menos comunes se organizan en módulos para que solo se carguen cuando las necesites.
                #TODO: Ejemplo:
                    #? Las operaciones matemáticas básicas como suma (+), resta (-), multiplicación (*) 
                    #? y división (/) están incluidas en el núcleo porque son fundamentales.
                    
                    #? Pero funciones como sqrt() o sin() están en el módulo math porque no todos los programas
                    #? necesitan cálculos matemáticos avanzados.



#TODO: 2. Eficiencia y carga de memoria
#? Al cargar solo los módulos que necesitas, Python optimiza el uso de memoria y recursos.
#? Si todo estuviera cargado por defecto, el tiempo de inicio de Python sería más lento y consumiría más memoria, 
#? incluso para programas simples.
                #TODO: Ejemplo:
                    #? Si escribes un programa para leer un archivo, probablemente no necesitas funciones 
                    #? matemáticas avanzadas. Mantenerlas fuera del núcleo evita cargar funcionalidades innecesarias.



#TODO: 3. Organización y modularidad
#?Python organiza las funcionalidades en módulos para hacerlas más fáciles de mantener y documentar.
#?Los módulos especializados agrupan funciones relacionadas, lo que hace más intuitivo buscar 
#? y entender las herramientas disponibles.
                #TODO: Ejemplo:
                    #?lo relacionado con operaciones matemáticas avanzadas está en math.
                    #?Funciones relacionadas con manejo de fechas y horas están en datetime.
                    #?Esto también permite que la comunidad extienda Python con módulos adicionales.



#TODO: 4. Evitar conflictos de nombres
#?Si todas las funciones posibles estuvieran disponibles en el espacio de nombres global, sería más probable que se
#? produjeran conflictos con los nombres de las variables o funciones que definas en tu programa.
                #TODO: Ejemplo:
                    #? Si escribes una función llamada log() en tu código, podría entrar en conflicto con una 
                    #? función log() predefinida si estuviera siempre disponible en el núcleo. 
                    #? Al estar en un módulo (math.log()), puedes evitar estos conflictos.


#TODO: 5. Facilidad para ampliar funcionalidades
#? - Al mantener el núcleo de Python pequeño y delegar funcionalidades avanzadas a módulos, es más fácil actualizar 
#? o reemplazar esos módulos sin afectar al lenguaje base.

#? - Los desarrolladores pueden agregar nuevos módulos o mejorar los existentes sin riesgo de romper el núcleo de Python.

#!En resumen, las funciones importadas están en módulos para que Python sea más modular, eficiente y fácil de usar, 
#! adaptándose a las necesidades de diferentes proyectos sin cargar innecesariamente el lenguaje base.

