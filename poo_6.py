print(" ")
print("Sanchez Perez Briana Sarahi, 1213, 3W")
print(" ")

class Marino:
    def hablar(self):
        print("Hola, soy un animal marino!")

class Pulpo(Marino):
    def hablar(self):
        print("Hola, soy un pulpo!")

class Foca(Marino):
    def hablar(self, mensaje):
        print(mensaje)

marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola, soy una foca!")

print(" ")