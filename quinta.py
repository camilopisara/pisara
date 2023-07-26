saldo = 1000000
def welcome():
    print("Bienvenido al banco felix")
    welcome()
    global debito
    

def opcion():
        print("1. retiro de tarjeta debito")
        print("2. avance de tarjeta de credito")
        print("3. consignar")
        print("4. depositar")
        opc = int(input("Escoja una opcion:"))
        
        if opc == 1:
            print("1. 10000")
            print("2. 20000")
            print("3. 50000")
            print("4. 100000")
            print("5. 150000")
            print("6. otra opcion")
            opc = int(input("escoje una opcion:"))
            password = int(input("ingrese la contraseña:"))
            
            
            
            if opc == 1:
                print(" acabas de reitirar:10000")
                saldo = saldo - 10000
                print("tu saldo actual es:", saldo)
        elif opc == 2:
                print(" acabas de reitirar:20000")
                saldo = saldo - 20000
                print("tu saldo actual es:", saldo)
        elif opc == 2:
                print(" acabas de reitirar:50000")
                saldo = saldo - 50000
                print("tu saldo actual es:", saldo)
        elif opc == 4:
                print(" acabas de reitirar:100000")
                saldo = saldo - 100000
                print("tu saldo actual es:", saldo)
        elif opc == 5:
                print(" acabas de reitirar:150000")
                saldo = saldo - 150000
                print("tu saldo actual es:", saldo)
        elif opc == 6:
            retiro = int(input("ingreseel valor a retirar:"))
            if retiro > saldo:
                print("lo siento, no puedes retirar esa cantidad de dinero")
            else:
                sal = saldo - retiro 
                print("acabas de retirar:", retiro)
                print("su saldo actual es:",sal)
                
opcion ()