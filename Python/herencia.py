class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

        # Proceso de limpieza de nombre y apellido

    def saludar(self):
        print(f"Hola mi nombre es: {self.nombre} {self.apellido}")


class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, turno):
        super().__init__(nombre, apellido, dni)
        self.turno = turno

    def inscribirse(self):
        print("Me inscribi a un curso")


class Docente(Persona):
    def __init__(self, nombre, apellido, dni, CUIT):
        super().__init__(nombre, apellido, dni)
        self.CUIT = CUIT

    def tomar_curso(self):
        print("Tomé un curso como docente")


class Egresado(Alumno):
    def __init__(self, nombre, apellido, dni, turno, año_egreso):
        super().__init__(nombre, apellido, dni, turno)
        self.año_egreso = año_egreso

alumno1 = Alumno("Carlos", "Lopez", 1234, "Noche")
alumno1.saludar()
alumno1.inscribirse()

docente1 = Docente("Maria", "Del Cerro", 5678, 1111)
docente1.saludar()
docente1.tomar_curso()

alumno1.nombre