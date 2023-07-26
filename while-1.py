numeros = []
while True:
    num = int(input("Ingrese un número entero positivo (0 para salir): "))
    if num == 0:
        break
    numeros.append(num)
if numeros:
    print(f"El mayor número ingresado es {max(numeros)}.")
else:
    print("No se ingresaron números.")