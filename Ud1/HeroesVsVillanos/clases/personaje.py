from datetime import date
class Personaje:


    _contador_id = 0 #variable de calse para el Id
    def __init__(self,nombre,apellidos,fecha_nacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        Personaje._contador_id*=1
        self.identificador = Personaje._contador_id
        #la edad debe ser date
        """
        como se que me lo vas a preguntar he estado buscando y
        utilizo "isinstance()" y no "type()" por uqe con isinstace maneja mejor la herencia
        por ejemplo si tienes una subclase de str, isinstance() devuelve true mientras que type() no"
        """
        if isinstance(fecha_nacimiento,str):
            self.fecha_nacimiento = date.fromisoformat(fecha_nacimiento) #transforma a date tipo iso YYYY-MM-DD
        else:
            self.fecha_nacimiento = fecha_nacimiento  #creo que este else puede sobrar pero por si acaso se introduce en otro formato
        self.puntuacion_total = 0

    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        # Ajustar si aún no ha cumplido años este año
        if hoy.month < self.fecha_nacimiento.month or \
                (hoy.month == self.fecha_nacimiento.month and hoy.day < self.fecha_nacimiento.day):
            edad -= 1
        return edad


    def __str__(self):
        return f"{self.nombre} {self.apellidos} {self.fecha_nacimiento}"
