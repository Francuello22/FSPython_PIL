# Funciones

# Tienen un nombre, argumentos, codigo y su salida o retorno

def sumar (a, b):

    resultado = a + b

    return resultado

print(sumar(2, 8))

# Tambien podemos tener funciones sin parametros, osea las harcodeamos y se respeta

def resta():

    resultado_r = 10 - 2

    return resultado_r

print(resta())

# Funcion sin retorno

def multiplicacion():

    print(5+5)

    return

multiplicacion()

#

def saludos(n):

    saludos = []

    for i in range (n):

        nombres = input("Ingrese nombre para saludo: ")
        print("Hola", nombres)
        saludos.append(nombres)
        
    print(saludos)
    return saludos



saludos(3)
        

    