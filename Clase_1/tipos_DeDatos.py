# STR cadenas 

print()
a = "Dua Lipa"
print(a, type(a))
print()

# INT 
b = 5
print(b, type(b))
print()

# Si yo quiero transformar un numero en cadena 
c = str(b)
print(c, type(c))
print()

# Si quiero mostrar determinada letra de una cadena utilizo indices empezando por 0
print("Cual es el quinto caracter en Dua Lipa: ", a[4])
print()

# Si quiero mostrar un intervalo de caradcteres
print("Mostrar solo el primer nombre de la cantante:", a[0:3])
print()

# Si quiero arrancar desde atras para adelante
print("Mostrar solo el segundo nombre de la cantante:", a[-4:-1])
print()

# Metodos del lenguaje para usar con PRINT


# Devuelve el largo o cantidad de caracteres de una cadena o lista, etc. - LEN()
print("Nuestra cadena: ", a, " tiene", len(a), "caracteres.")

# Para devovler toda una cadena en minuscula - LOWER()
print("Cadena normal: ", a)
print("Cadena en minusculas: ", a.lower())
print()
# Para devovler toda una cadena en minuscula - UPPER()
print("Cadena normal: ", a)
print("Cadena en mayusculas: ", a.upper())
print()
# Devovler la cadena separada por palabras en una lista - SPLIT()
print("Cadena normal: ", a)
print("Cadena separada en palabras: ", a.split())
print()
print("Nuestra cadena: ", a, " tiene", len(a), "caracteres", " ,pero la lista que obtuvimos: ", a.split(), "tiene: ", len(a.split()), ".")
print()

# LISTAS o VECTORES - separa elementos de cualquier tipo con comas
print("------------------------------------------------------------------------------------------------------")
Lista1 = ["Dua", "Lipa", 2, 4.5]
print("La lista contiene: ", Lista1)
print("La lista contiene: ", len(Lista1), " elementos.")
print("El segundo elemento de la lista es: ", Lista1[1])
print()

# Metodos del lenguaje para LISTAS

# Agregar elemnto al final de la lista - APPEND()
Lista1.append("Fornite")
print(Lista1)
print()
# Preguntar en qeu indice esta tal elemento - INDEX ()
print("El elemento 4.5 esta en el indice: ", Lista1.index(4.5), " de la lista.")
print()
# Agregar un nuevo elemento en el indice que querramos
Lista1.insert(3, "Lol")
print("La nueva lista es: ", Lista1)
print()

# DICCIONARIOS - Estructuras de datos muy similares a una clase en POO

usuario = {
            "Nombre" : "Franco",
            "Edad" : 21, 
            "Fecha de Nacimiento" : "22/09/2000",
            "Estado Civil" : False,
            "Mascotas" : ["Perro", "Gato"]
}

print(usuario)
print()
print("Las mascotas que tiene Franco son: ", usuario["Mascotas"])
print()

# Metodos del lenguaje para diccioarios

# Para mostrar determinado valor de una key de un diccionario al igual que hicimos arriba
print("La edad de Franco es: ", usuario.get("Edad"))
print()
# pero tambien nos sirve para que si no encuentra determinada key, devuelve el valor que le asignemos
print("Franco es hincha de: ", usuario.get("Hincha de", "INDEPENDIENTE"))
print()
# Saber todas las llaves/keys de un dicionario
print("Las keys de este diccionario son: ", usuario.keys())
print()
# ya que nos devuelve una "lista" de las keys del diccionario, podemos guardarla en una variable para utilizarla
# pero NO es una lista aunque lo parezca, por esto la tranformamos con list()
lista_Keys_Usuario = list(usuario.keys())
print("La segunda key de usuarios es: ", lista_Keys_Usuario[1],  " y es: ", usuario.get("Edad"), ".")
print()
#Tambien podemos obtener una "lista" con los valores de las keys, tambien voy a tener que usar list() para convertirlo en lista
lista_Valores_Usuario = list(usuario.values())
print("El estado civil de Franco es: ", lista_Valores_Usuario[3])
print()
