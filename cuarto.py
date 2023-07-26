def cajero():
    saldo = 100000
    clave = 1950
    intentos = 0
    
    while True:
        if intentos == 3:
            print("Ha excedido el número máximo de intentos permitidos.")
            break
        else:
            pin = int(input("Ingrese su clave: "))
            if pin == clave:
                print("Bienvenido al cajero automático.")
                print("1. Consultar saldo")
                print("2. Retirar dinero")
                print("3. Salir")
                opcion = int(input("Ingrese una opción: "))
                if opcion == 1:
                    print(f"Su saldo actual es {saldo}.")
                elif opcion == 2:
                    monto = int(input("Ingrese el monto a retirar: "))
                    if monto > saldo:
                        print("Fondos insuficientes.")
                    else:
                        saldo -= monto
                        print(f"Retire su dinero. Su saldo actual es {saldo}.")
                elif opcion == 3:
                    break
                else:
                    print("Opción inválida.")
            else:
                intentos += 1
                print(f"Clave incorrecta. Intento {intentos} de 3.")
cajero()