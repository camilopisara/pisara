pares = 0
while True:
    n = int(input("Ingrese un número positivo (-1 para terminar): "))
    if n == -1:
        break
    suma = 0
    while n > 0:
        digito = n % 10
        suma += digito
        n //= 10
    print("Suma de los dígitos:", suma)
    if suma % 2 == 0:
        pares += 1

print("Cantidad de números pares ingresados:", pares)