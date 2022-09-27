

# PDF 2 - Ejercicio 1 - Realizar menu de opciones

saldo = 0
op = 0

while op <= 4 :

    print("----------------------------------------------------------------")
    print("---------------------  BANCO CUELLO  ---------------------------")
    print("----------------------------------------------------------------")
    print()
    print("Seleccione una opcion: ")
    print("1 - DEPOSITO")
    print("2 - TRANSFERENCIA")
    print("3 - EXTRACCION")
    print("4 - SALIR")
    print()
    print("----------------------------------------------------------------")
    print()

    op = int(input("Elegir la opcion deseada: "))
    print()
    if op > 4:
        print("La opcion seleccionada no es correcta. Porfavor elija nuevamente.")
        op = 0
        print()
        
    else:
        if op == 1:
            print("-----------------  DEPOSITO  --------------------")
            print()
            print("Su saldoa actual es de: $", saldo)
            print()
            saldo += int(input("Cuanto dinero desea ingresar a la cuenta?: "))
            print()
            print("Su nuevo saldo es de: $", saldo)
            print()


        if op == 2:
            print("--------------  TRANSFERENCIA  ------------------")
            print()
            print("Su saldo actual es de: $", saldo)
            print()
            if saldo == 0:
                print("No posee dinero todavia en su cuenta, porfavor primero realice un deposito.")
                print("")
            else: 
                 nom = input("Nombre del destinatario: ")
                 print()
                 tra = int(input("Ingrese la cantidad de dinero a transferir: "))
                 print()
                 op2= 0
                 print("Usted va a tranferirle a ", nom, " $", tra)
                 print()
                 print("Desea continuar? ")
                 op2 = input("Escriba SI o NO : ")
                 if op2 == "SI" or "si" or "Si":
                     saldo -= tra
                     print()
                     print("Su nuevo saldo es de: $", saldo)
                     print()
                 elif op2 == "NO" or "No" or "no":
                     print("La operacion no se ha realizado. Porfavor ezcoja otra opcion nuevamente.")
                 else:
                     print("No ha escogido una opcion correcta. Porfavor elija otra.")



        if op == 3:
            print("--------------- EXTRACCION  ---------------------")
            print()
            print("Su saldo actual es de: $", saldo)
            print()
            if saldo == 0:
                print("No posee dinero todavia en su cuenta, porfavor primero realice un deposito.")
                print("")
            else:
                ex = int(input("Indique cantidad de dinero a extraer: "))
                print("Su nuevo saldo sera de: $", saldo - ex, "Si desa continuar escriba SI, de lo contrario NO.")
                print("")
                op3 = input("Escriba la opcion seleccionada: ")
                if op3 == "SI" or "si" or "Si":
                    saldo -= ex
                    print()
                    print("Su nuevo saldo es de: $", saldo)
                    print()
                elif op2 == "NO" or "No" or "no":
                    print("La operacion no se ha realizado. Porfavor ezcoja otra opcion nuevamente.")
                else:
                    print("No ha escogido una opcion correcta. Porfavor elija otra.")


        if op == 4:
            print("-----------------  SALIR -------------------")
            print()
            print("Gracias por utilizar nuestro sistema")
            print()
            break
    


# PDF 2 - Ejercicio 2 - Identificar numeros pares dentro de un rango
