print(" ")
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")

class Universidad:
    def __init__(self, nombre):
        self.nombre_universidad = nombre

class Carrera:
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(
            f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, "
            f"su especialidad es {self.especialidad}. Estudia en la universidad {self.nombre_universidad}."
        )

persona = Estudiante("Harvard")
persona.carrera("Ingeniería mecatrónica")
persona.datos("Mike", 19)

print(" ")