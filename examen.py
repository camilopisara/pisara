def calcular_precio_total(opcion_galaxy_note):
    precios_galaxy_note = {1: 1000000, 2: 1500000, 3: 2000000}
    precios_accesorios = {
        "Audifonos": 15000,
        "Cargador": 13000,
        "Estuche": 5000
    }

    precio_galaxy_note = precios_galaxy_note.get(opcion_galaxy_note)
    if not precio_galaxy_note:
        print("Opción de Galaxy Note inválida.")
        return

    print(f"Precio del Galaxy Note: {precio_galaxy_note} millones")

    total_accesorios = sum(precios_accesorios[accesorio] for accesorio in precios_accesorios if input(f"¿Desea agregar {accesorio}? (s/n): ").lower() == 's')

    precio_total = precio_galaxy_note + total_accesorios

    print("\nDetalle de la compra:")
    print(f"Precio del Galaxy Note: {precio_galaxy_note} millones")
    print("Accesorios seleccionados:")
    for accesorio in precios_accesorios:
        if accesorio.lower() in ("audifonos", "cargador", "estuche"):
            print(f"{accesorio}: {precios_accesorios[accesorio]} millones")

    print(f"\nPrecio total con accesorios: {precio_total} millones")

# Main
print("Bienvenido a Samsung")
print("Opciones de Galaxy Note:")
print("1) Galaxy Note S")
print("2) Galaxy Note T")
print("3) Galaxy Note W")

opcion_galaxy_note = int(input("Seleccione el Galaxy Note (1, 2 o 3): "))
calcular_precio_total(opcion_galaxy_note)
