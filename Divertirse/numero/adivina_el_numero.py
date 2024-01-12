import random


def adivina_el_número(x):
    
    print("===========================")
    print(" ¡Bienvenido(a) al juego!")
    print("===========================")
    print("Tu meta es adivinar el número generado por la computadora.")

    numero_aleatorio = random.randint(1, x) #Número aleatorio entre 1 y x.

    predicción = 0

    while predicción != numero_aleatorio:
        # Usuario ingresa un número
        predicción = int(input(f"Adivina un número entre 1 y {x}: "))

    if predicción < numero_aleatorio:
        print ("Intenta otra vez. Este número es muy pequeño.")
    elif predicción > numero_aleatorio:
        print ("Intnta otra vez. Este número es muy grande.")
    print (f" ¡Felicidades! Adivinaste el número {numero_aleatorio} correctamente")

adivina_el_número(10)