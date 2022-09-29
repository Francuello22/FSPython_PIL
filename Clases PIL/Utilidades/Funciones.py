# # Funciones

# # Tienen un nombre, argumentos, codigo y su salida o retorno

# def sumar (a, b):

#     resultado = a + b

#     return resultado

# print(sumar(2, 8))

# # Tambien podemos tener funciones sin parametros, osea las harcodeamos y se respeta

# def resta():

#     resultado_r = 10 - 2

#     return resultado_r

# print(resta())

# # Funcion sin retorno

# def multiplicacion():

#     print(5+5)

#     return

# multiplicacion()

# #

# def saludos(n):

#     saludos = []

#     for i in range (n):

#         nombres = input("Ingrese nombre para saludo: ")
#         print("Hola", nombres)
#         saludos.append(nombres)

#     print(saludos)
#     return saludos

# saludos(3)

# Podemos otorgar argumentos en base a la posicion de entrada

# def prueba (a, b, c):
#     print(a, b, c)


# a = 1
# b = 2
# c = 3

# prueba(b, c, a)

# Como vemos, el codigo no respeta nuestra funcion, imprimiedo en el orden que nosotros le entreguemos los argumentos
# Una solucion seria tener cuidado al ingresar los argumentos, y otra seria definirlos de la siguiente manera


def prueba2(a, b, c):
    print(a, b, c)


a = 1
b = 2
c = 3

prueba2(b=b, c=c, a=a)

# Y de esta forma como vemos, a pesar de modifricar el orden de entrada de los argumentos, se respeta la funcion

# Tipo de formato para documentar funciones o simplemente con 3 comillas dobles """Esta funcion realiza ..."""

"""_summary_

    Args:
        x (_type_): _description_

    Returns:
        _type_: _description_
    """
