# Variales nos permiten asignar lugar en memoria para ayudarnos solamente con "="

Numero1 = input("Ingrese un numero: ")
Numero2 = input("Ingrese otro numero: ")
Resultado = Numero1 + Numero2
print("La varibale Numero 1 es de tipo: ", type(Numero1))
print(Resultado)

# Con Type() podemos ver que tipo de variable tenemos
# Para solucionar la concatenacion cuando queremos realizar una operacion como en el ejemplo 
# anterior debemos utilizar int para transformar en enteros esa cadena

Numero1 = int(input("Ingrese un numero: "))
Numero2 = int(input("Ingrese otro numero: "))
Resultado = Numero1 + Numero2
print("El resultado es de la suma es: ", Resultado)


 #  "hola"