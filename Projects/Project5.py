# El ahorcado / The hanged

import random
import string

from Project5_words import words
from Project5_lives import lifes_dictionary_diagram
from Project5_phrases import phrases

def get_valid_word(list_words):
    word = random.choice(list_words)
    while '-' in word or ' ' in word:
        word = random.choice(list_words)
    return word.upper()

def get_valid_phrase(list_phrases):
    phrase = random.choice(list_phrases)
    return phrase  # Asegúrate de devolver la frase seleccionada

def hanged():
    print("======================================")
    print(" ¡Bienvenido/a al juego del Ahorcado! ")
    print("======================================")

    word = get_valid_word(words)
    phrase = get_valid_phrase(phrases)

    # Verificar si la palabra obtenida es válida (no None)
    if word is None:
        print("Error al obtener la palabra. Terminando el juego.")
        return
    
    # Verificar si la frase obtenida es válida (no None)
    if phrase is None:
        print("Error al generar la frase. Terminando el juego.")
        return

    letters_to_guess = set(word)  # Conjunto de letras de la palabra a adivinar
    guessed_letters = set()  # Conjunto de letras ya adivinadas
    alphabet = set(string.ascii_uppercase)  # Conjunto de letras del abecedario
    lifes = 7  # Número de vidas restantes

    while len(letters_to_guess) > 0 and lifes > 0:
        # Mensaje de vidas restantes (singular o plural)
        lives_message = f"Te queda {lifes} vida" if lifes == 1 else f"Te quedan {lifes} vidas"
        
        # Mostrar el estado del juego
        print(f"{lives_message} {phrase}: {' '.join(guessed_letters)}")
        word_list = [letter if letter in guessed_letters else '-' for letter in word]
        print(lifes_dictionary_diagram[lifes])
        print(f"Palabra: {''.join(word_list)}")

        # Obtener la letra del usuario
        user_letter = input("Escoge una letra: ").upper()

        # Validar la letra ingresada
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)

            # Comprobar si la letra está en la palabra
            if user_letter in letters_to_guess:
                letters_to_guess.remove(user_letter)
                print('')
            else:
                lifes -= 1
                print(f"\nTu letra, {user_letter} no está en la palabra.")

        elif user_letter in guessed_letters:
            print("\nYa escogiste esa letra. Por favor, escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

    # Fin del juego: se adivinó la palabra o se perdieron todas las vidas
    if lifes == 0:
        print(lifes_dictionary_diagram[lifes])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho 🥺. La palabra era: {word}")
    else:
        print(f"¡Excelente! ¡Adivinaste la palabra {word} 😊!")

hanged()
