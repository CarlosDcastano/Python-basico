class Persona:
    def __init__(self, nombre, edad, rol):
        self.nombre = nombre
        self.edad = edad
        self.rol = rol
     
    def cambiar_nombre(self, newname):
        if not newname.strip():
            print("El nuevo nombre no puede estar vacío")
        else:
            self.nombre = newname
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, rol, semestre):
        super().__init__(nombre, edad, rol)
        self.semestre = semestre
        
p1 = Persona("Miguel", 25, "Docente")
e1 = Estudiante("Antonio", 21, "Estudiante", 6)

print(f"Hola, su nombre es {p1.nombre}, su edad es {p1.edad}, y eres un {p1.rol}")
print(f"Hola, su nombre es {e1.nombre}, su edad es {e1.edad}, eres un {e1.rol} y estás en el semestre # {e1.semestre}")

p1.cambiar_nombre("Lucas")
e1.cambiar_nombre()
print(f"Hola, su nombre es {p1.nombre}, su edad es {p1.edad}, y eres un {p1.rol}")
print(f"Hola, su nombre es {e1.nombre}, su edad es {e1.edad}, eres un {e1.rol} y estás en el semestre # {e1.semestre}")