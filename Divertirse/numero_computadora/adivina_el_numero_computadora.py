import random


def adivina_el_núero_computadora(x):
    
    print("............................")
    print("  ¡Bienvenido(A) al juego!")
    print("............................")

    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo...")

    limite_inferior = 1
    limite_superior = x
    respuesta = ""
    while respuesta != "c":
        if limite_inferior != limite_superior:
            predicción = random.randint(limite_inferior, limite_superior)
        else:
            predicción = limite_superior
        
        respuesta = input(f"Mi predicción es {predicción}. Si es muy alta, ingresa (A). Si es muy baja, ingresa(B). Si es correcto ingresa (C) ").lower()

        if respuesta == "a":
            limite_superior = predicción -1
        elif respuesta == "b":
            limite_inferior = predicción +1
    print(f" La computadora adivino tu número correctamente: {predicción}")

adivina_el_núero_computadora(10)

