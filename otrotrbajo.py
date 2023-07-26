def cajero():
    saldo_debito = 100000  # Debit card balance
    saldo_credito = 50000  # Credit card balance
    password = "mypassword"  # Replace "mypassword" with your actual password
    max_attempts = 3

    def verify_password():
        nonlocal max_attempts
        attempts = 0

        while attempts < max_attempts:
            input_password = input("Ingrese la contraseña: ")
            if input_password == password:
                return True
            else:
                attempts += 1
                remaining_attempts = max_attempts - attempts
                if remaining_attempts > 0:
                    print(f"Contraseña incorrecta. Te quedan {remaining_attempts} intentos.")
                else:
                    print("Has excedido el número de intentos. Vuelve a iniciar el programa.")
                    return False
        return False

    if not verify_password():
        return

    while True:
        print("Bienvenido al cajero automático.")
        print("1. Consultar saldo de tarjeta débito")
        print("2. Consultar saldo de tarjeta de crédito")
        print("3. Retirar dinero")
        print("4. Cambiar contraseña")
        print("5. Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            print(f"El saldo de su tarjeta débito es {saldo_debito}.")
        elif opcion == 2:
            print(f"El saldo de su tarjeta de crédito es {saldo_credito}.")
        elif opcion == 3:
            monto = int(input("Ingrese el monto a retirar: "))
            if monto <= saldo_debito:
                saldo_debito -= monto
                print(f"Retire su dinero. Su saldo actual es {saldo_debito}.")
            else:
                print("Fondos insuficientes.")
        elif opcion == 4:
            new_password = input("Ingrese la nueva contraseña: ")
            password = new_password
            print("Contraseña cambiada exitosamente.")
        elif opcion == 5:
            print("Gracias por usar nuestro cajero automático.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

cajero()
