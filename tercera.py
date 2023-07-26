def my_fuction():
    print("Bienvenido al banco")
    password = "1590"
    saldo = 100000
    retiro = 100000 

    contra = input("password: ")

    if password == contra:
        print("Bienvenido!")
        print("Su saldo es:", saldo)
        
        opciones = int(input("opciones:\n1. 200000 \n2. 40000  \n3.60000 \n4. 80000 \n5. 100000\n6. retiro\n 7. 2000000 \n"))
        
        def debitofn():
            if opciones == 1:
                if saldo >= 200000:
                    saldo -= 200000
                    print("¡Retiro exitoso!")
                else:
                    print("Fondos insuficientes.")
            elif opciones == 2:
                if saldo >= 30000:
                    saldo -= 30000
                    print("¡Retiro exitoso!")
                else:
                    print("Fondos insuficientes.")
            elif opciones == 3:
                if saldo >= 40000:
                    saldo -= 40000
                    print("¡Retiro exitoso!")
                else:
                    print("Fondos insuficientes.")
            elif opciones == 4:
                if saldo >= 50000:
                    saldo -= 50000
                    print("¡Retiro exitoso!")
                else:
                    print("Fondos insuficientes.")
            elif opciones == 5:
                if saldo >= 60000:
                    saldo -= 60000
                    print("¡Retiro exitoso!")
                else:
                    print("Fondos insuficientes.")
            elif opciones == 6:
                if saldo >= 70000:
                    saldo -= 70000
                    print("¡Retiro exitoso!")
                else:
                    print("fondos insuficientes.")
            else:
                print("contraseña invalida.")
            
    elif opciones == 7:
            if saldo >= retiro:
                    saldo = saldo - retiro
            debitofn()
        
my_fuction()