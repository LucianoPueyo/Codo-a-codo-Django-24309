class Alumno:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def alta(self):
        print(f"El alumno {self.nombre} {self.apellido} se dió de alta en un curso")

    def __eq__(self, other):
        return self.dni == other.dni


class Docente:
    def __init__(self, dni):
        self.dni = dni

    def __eq__(self, other):
        return self.dni == other.dni


alumno1 = Alumno(nombre="Carlos", apellido="Lopez", dni=1234)
alumno2 = Alumno("Maria", "Del Cerro", 5678)
alumno3 = Alumno("Gaston", "Perez", 1234)

docente1 = Docente(5678)

print(alumno1.nombre, alumno1.apellido)

alumno1.alta()
alumno2.alta()

print(alumno1 == alumno2)
print(alumno1 == alumno3)
print(alumno1 == docente1)