def my_function():
    print("hola usuario")
    opciones= int (input("elegir opcion"))
    v_retiro=int(input("ingrese a retirar:"))
    password=int(1590)
    saldo=int(100000)
    contra=int(input("ingresa contraseña:"))
    if password == contra:
        if v_retiro > saldo:
            print("saldo insuficiente:")
    else:
        print("retiro exitoso")
    
    nuevo_saldo = saldo - v_retiro
my_function()