# Piedra, papel y tijeras / rock, paper and scissors

import random


def play():
    user = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()
    computer = random.choice(['pi', 'pa', 'ti'])

    if user == computer:
        return f'¡Empate!\n La compuradora eligió también {computer}.'
            
    elif win_player(user, computer):
        return f'¡Ganaste!\n La computadora eligió {computer}.'
    
    else:
        return f'¡Perdiste!\n La computadora eligió {computer}.'

def win_player(player, opponent):
    # Retornar True (verdadero) si gana el jugador.
    # Piedra gana a Tijera(pi > ti).
    # Tijera gana a Papel (ti > pa).
    # Papel gana a Piedra (pa > pi).
    if ((player == 'pi' and opponent == 'ti')
        or (player == 'ti' and opponent == 'pa')
        or (player == 'pa' and opponent == 'pi')):
        return True
    else:
        return False
    

print(play())
