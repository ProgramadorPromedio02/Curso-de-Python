# Adivina el número(Guess the Number)

import random


def guess_number(x):
  print("===========================")
  print("  ¡Bienvenido/a al Juego!  ")
  print("===========================")
  print("Tu meta es adivinar el número generado por la computadora.")

  num_random = random.randint(1, x) # Número aleatorio entre 1 y x.

  predixion = 0

  while predixion != num_random:
    # El usuario ingresa un número
    predixion = int(input(f"Adivina un número entre 1 y {x}: ")) # f-string

    if predixion < num_random:
      print("Intenta otra vez. Este número es muy pequeño.")
    elif predixion > num_random:
      print("Intenta otra vez. Este número es muy grande.")

  print(f"¡Felicitaciones! Adivinaste el número {num_random} correctamente :).")


guess_number(10)

