import random


def jugar ():
    usuario = input("Escoge una opcion: .pi. para piedra, .pa. para papel, .ti. para tijera.\n").lower()
    computadora = random.choice(['pi','pa','ti'])

    if usuario == computadora: 
        return ' ¡Empate! '
    if ganó_el_jugador(usuario, computadora):
        return ' ¡Ganaste! '
    
    return ' ¡Perdiste! '


def ganó_el_jugador (juegador, oponente):
    if((juegador == 'pi' and oponente == 'ti')
       or (juegador == 'ti' and oponente == 'pa')
       or (juegador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False
    

print(jugar())