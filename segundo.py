def my_function ():
   
 opciones_1 = int (input( "bienvenido al banco Felix de Bedout Moreno \n 1.retiro t.debito \n 2.avance t.c \n 3.consignación \n 4.pago \n elegir opción de tarea : "));

 if opciones_1 == 1:
    print("retiro de tarjeta de debito");

 if opciones_1 == 2:
    avance_tc();

 if opciones_1 == 3:
    print("consignación");

 if opciones_1 == 4:
    print("pago");

 if opciones_1 < 1 or opciones_1 > 7:
    print("operacion no valida");

def avance_tc():
    print("avance t.c");

def debitofn():
    password = int (1590);
    debito = int (100000);
    credito = int (2000000);

    print("valor a retirar: \n 1. 20000 \n 2. 50000 \n 3. 100000 \n 4. 200000 \n 5. 600000 \n 6. 1200000 \n 7. otros")
    opciones_2 = int (input("elegir opción "));


    contra = int (input("ingresa contraseña "));   
    

    if password == contra:

        if opciones_2 == 1 and 20000 > debito:
            print("saldo insuficiente");
        elif opciones_2 == 2 and 50000 > debito:
            print("saldo insuficiente");
        elif opciones_2 == 3 and 100000 > debito:
            print("saldo insuficiente");
        elif opciones_2 == 4 and 200000 > debito:
            print("saldo insuficinte");
        elif opciones_2 == 5 and 500000 > debito:
            print("saldo insuficiente");
        elif opciones_2 == 6 and 1200000 > debito:
            print("saldo insuficiente");
        elif opciones_2 == 7:
          v_retiro = int (input("ingrese valor a retirar "));

          if v_retiro > debito:
            print ("saldo insuficiente");
          else:
            print("retiro exitoso");
        else:
            print("retiro exitoso")

    else:
        print("contraseña incorrecta");

my_function()

debitofn()
