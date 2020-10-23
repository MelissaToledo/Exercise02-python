from Exercise02 import Finanzas, ingresos, egreso

saldo = 0.0
listaIng = []
listatEg = []

while True:
    option = input(
        "¡Bienvenido a tu cuenta bancaria!\nMenu: \n0-Salir \n1-Ingresar dinero a la cuenta\
        \n2-Retirar dinero de la cuenta \n3-Ver reporte de ingresos \n4-Ver reporte de egresos\
        \n5-Ver reporte de todas las transacciones \n6-Ver saldo total \nIngrese una opcion:"
    )

    if option == "0":
        print("¡Gracias por usar nuestro programa para tus finanzas personales!")
        print("-" * 100)
        break

    elif option == "1":
        montoIng = float(input("¿Cuanto dinero desea ingresar?...$"))
        listaIng.append(montoIng)
        ingreso1 = ingresos(montoIng)
        resultIng = ingreso1.addIngreso()
        saldo = saldo + resultIng
        print(f"Ingreso exitosamente a su cuenta: $", resultIng)
        print(f"El saldo actual de la cuenta es ${saldo}")
        print("-" * 100)

    elif option == "2":
        montoEg = float(input("¿Cuanto dinero desea retirar?...$"))
        if saldo < montoEg:
            print("Error: No hay suficientes fondos, su saldo pendiente sera negativo")
            listatEg.append(montoEg)
            egreso1 = egreso(montoEg)
            resultEg = egreso1.addEgreso()
            saldo = saldo + resultEg
            print(f"Retiro de su cuenta: $", resultEg)
            print(f"El saldo actual de la cuenta es ${saldo}")
            print("-" * 100)
        else:
            listatEg.append(montoEg)
            egreso1 = egreso(montoEg)
            resultEg = egreso1.addEgreso()
            saldo = saldo + resultEg
            print(f"Retiro existosamente de su cuenta: $", resultEg)
            print(f"El saldo actual de la cuenta es ${saldo}")
            print("-" * 100)

    elif option == "3":
        print("El reporte de todos sus ingresos es:")
        for iterator in listaIng:
            print(iterator)
        print("-" * 100)

    elif option == "4":
        print("El reporte de todos sus egresos es:")
        for iterator in listatEg:
            print(iterator)
        print("-" * 100)

    elif option == "5":
        print("Reporte de todas sus transacciones")
        print("El reporte de todos sus ingresos es:")
        for iterator in listaIng:
            print(iterator)
        print("El reporte de todos sus egresos es:")
        for iterator in listatEg:
            print(iterator)
        print("-" * 100)

    elif option == "6":
        print(f"Saldo disponible en su cuenta: ${saldo}")
        print("-" * 100)
