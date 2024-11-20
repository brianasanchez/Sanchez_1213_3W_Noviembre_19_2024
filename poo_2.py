print(" ")
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")

class Persona: 
    def __init__(self, nombre, edad): 
        self.nombre = nombre 
        self.edad = edad 

    def cumpleaños(self): 
        self.edad += 1 

p = Persona("Nombre", 25)  
p.cumpleaños() 
print(f"{p.nombre} cumple {p.edad} años") 

print(" ")