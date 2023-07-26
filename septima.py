
def cajero():
    saldo = 100000
    
    while True:
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
            elif monto >= 20000 and monto <= 1200000:
                if monto == 20000:
                    saldo -= monto
                    print(f"Retire su dinero. Su saldo actual es {saldo}.")
                elif monto == 40000:
                    saldo -= monto
                    print(f"Retire su dinero. Su saldo actual es {saldo}.")
                elif monto == 60000:
                    saldo -= monto
                    print(f"Retire su dinero. Su saldo actual es {saldo}.")
                elif monto == 80000:
                    saldo -= monto
                    print(f"Retire su dinero. Su saldo actual es {saldo}.")
                elif monto == 100000:
                    saldo -= monto
                    print(f"Retire su dinero. Su saldo actual es {saldo}.")
                elif monto == 1200000:
                    saldo -= monto
                    print(f"Retire su dinero. Su saldo actual es {saldo}.")
            else:
                print("Monto inválido.")
        elif opcion == 3:
            break
        else:
            print("Opción inválida.")

cajero()

