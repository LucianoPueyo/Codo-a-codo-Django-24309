class Circulo:
    def dibujar(self):
        print("☺")

class Rectangulo:
    def dibujar(self):
        print("#")

class Triangulo:
    def dibujar(self):
        print("♠")


figuras = [Circulo(), Rectangulo(), Triangulo()]

for figura in figuras:
    figura.dibujar()
