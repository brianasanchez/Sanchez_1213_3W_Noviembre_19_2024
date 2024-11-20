print(" ")
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")

class Estudiante: # Define una clase
    def __init__(self, nombre, nota): 
        self.nombre = nombre 
        self.nota = nota 

    def imprimir(self): # Define un método
        print(f"Nombre: {self.nombre} \nNota: {self.nota}") 

    def resultados(self): 
        if self.nota >= 7: 
            print("¡Has APROBADO!") 
        else: 
            print("¡Has REPROBADO!")

estudiante1 = Estudiante("Pedro", 5) 
estudiante1.imprimir() 
estudiante1.resultados() 

estudiante2 = Estudiante("Elizabeth", 7)
estudiante2.imprimir() 
estudiante2.resultados() 

print(" ")