import random

def guess_number_cpu(x):
    print("=========================")
    print(" ¡Bienvenido/a al Juego! ")
    print("=========================")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo.")

    limit_bottom = 1
    limit_top = x

    response = ""
    while response != "c":
        # Generar predicción
        if limit_bottom != limit_top:  # [1, 10]
            predixion = random.randint(limit_bottom, limit_top)
        else:
            predixion = limit_bottom  # también podría ser el límite superior

        # Obtener respuesta del usuario
        response = input(f"Mi predicción es {predixion}. Si es muy alta, ingresa (A) para restar. Si es muy baja, ingresa (B) para sumar. Si es correcta, ingresa (C): ").lower()

        if response == "a":
            limit_top = predixion - 1
        elif response == "b":
            limit_bottom = predixion + 1
        
        # Verificación de errores de límites
        elif limit_bottom > limit_top:
            print("❌Error❌: El límite inferior no puede ser mayor al límite superior.")
            break

    if response == "c":
        print(f"¡Excelente! La computadora adivinó tu número correctamente: {predixion}")

guess_number_cpu(10)
