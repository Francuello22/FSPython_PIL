
# Para crear una clase definimos atributos y funciones:

from msilib.schema import tables


class Perro:

    # Atributos de instancias GLOBALES, es decir, para TODOS los perros
    especie = "Mamiferos"

    # Constructor
    def __init__(self, nombre, edad, raza):
        # Con la variable SELF lo que hacemos es autoreferenciar la clase. Ej, el NOMBRE de ESTA clase la llamamos NOMBRE
        # Atributos de instacncias locales, es decir, es para CADA perro en particular
        self.nombre = nombre
        self. edad = edad
        self.raza = raza

    # Funciones del perro
    def ladrar(self):
        print("Guauuu")

    def jugar(self, objeto):
        print(self.nombre, " esta jugando con: ", objeto)


perro1 = Perro("Firpo", 10, "Ovejero Aleman")

print("El nombre del perro es: ", perro1.nombre,
      "La edad: ", perro1.edad, "La raza: ", perro1.raza, "Especie: ", perro1.especie)
perro1.ladrar
perro1.jugar("una piedra")


# Tambien podemos crear clases con atributos o constructores vacios, para que sean instaciados una vez se cree el objeto
class Vacas:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.peso = 0


vaca1 = Vacas()
vaca1.nombre = "Lola"
vaca1.edad = 12
vaca1.peso = 655
print("El nombre de la vaca es: ", vaca1.nombre, "edad: ",
      vaca1.edad, "años y su peso es de: ", vaca1.peso, "kg.")


# Podemos tambien tener clases padres donde sus clases hijas pueden HEREDAR atributos o comportamientos

class Animales:

    def __init__(self, cant_patas):
        self.cant_patas = cant_patas

# Entonces para poder utliizar este atributo en nuestra clase hija, debemos declarar en la entrada () que esa clase (hija) hereda de la otra. Ej.


class Gato(Animales):

    def __init__(self, nombre, raza, cant_patas):
        self.nombre = nombre
        self.raza = raza
# Ahora para instanciar el atributo de la CLASE PADRE a HEREDAR utlizamos la funcion SUPER()
        super().__init__(cant_patas)


gato1 = Gato("Astro", "Callejero", 4)
print("El nombre del gato es: ", gato1.nombre, ", su raza:",
      gato1.raza, ", y su cantidad de patas es de: ", gato1.cant_patas)
