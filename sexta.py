def cajero():
    saldo = 100000
    clave = 1950
    intentos = 0
    
    while True:
        if intentos == 3:
            print("Ha excedido el número máximo de intentos permitidos.")
            break
        else:
            monto = int(input("Ingrese el monto a retirar: "))
            if monto > saldo:
                print("Fondos insuficientes.")
            elif monto >= 20000 and monto <= 1200000:
                pin = int(input("Ingrese su clave: "))
                if pin == clave:
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
                    intentos += 1
                    print(f"Clave incorrecta. Intento {intentos} de 3.")
            else:
                print("Monto inválido.")

cajero()

