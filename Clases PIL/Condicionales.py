
# Estructura Condicional IF
print("----------------------------------------------------------------------------")
print()
a = int(input("Ingrese un numero a comparar: "))
b = int(input("Ingrese otro numero a comparar: "))

print("Los numero ingreasdos son: ", a ,"y", b)

if a > b :
    print("El numero mas grande es a: ", a)

else:
        print("El numero mas grande es b: ", b)
        print()
        print()

# Estructur de IF con AND porque tengo mas de una condicion
print("----------------------------------------------------------------------------")
print()
a = int(input("Ingrese un numero a comparar: "))
b = int(input("Ingrese el segundo numero a comparar: "))
c = int(input("Ingrese el tercer numero a comparar: "))

print("Los numero ingreasdos son: ", a ,",", b, "y", c)

if a > b and a > c :
    print("El numero mas grande es a: ", a)

elif  b > c:
        print("El numero mas grande es b: ", b)
else:
    print("El numero mas grande es c: ", c)
    print()

# Anidando IF sin usar AND
    print("----------------------------------------------------------------------------")
print()
a = int(input("Ingrese un numero a comparar: "))
b = int(input("Ingrese el segundo numero a comparar: "))
c = int(input("Ingrese el tercer numero a comparar: "))

print("Los numero ingreasdos son: ", a ,",", b, "y", c)

if a > b :
    if a > c:
        print("El numero mas grande es a: ", a)
elif b > c:
        print("El numero mas grande es b:", b)
else:
    print("El numero mas grande es c:", c)

    # == para comparar igualdades
    # != para comparar diferencias
    # > < para comparar magnitudes
    # >= <= para comparar igualdades O magnitudes
    # AND se deben para cumplir todas condiciones (&)
    # OR se debe cumplir una de las condiciones 


    


