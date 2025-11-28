# 3. Loop Control(break, continue, passs)

# These keywords help you control how loops behave
# Estas palabras clave te ayudan a controlar el comportamiento de los bucles.

# break: exit the loop early
#break: salir del bucle antes de tiempo

# continue: skips to the next iteration
# continuar: salta a la siguiente iteración

#pass: does nothing (used as a placeholder
#pasar: no hace nada (se usa como marcador de posición)

for num in range(1,10):
    if num == 5:
        break
    print(num)

print('\n')
for num in range(1,6):
    if num == 3:
        continue
    print(num)
print('\n')

for num in range(3):
    if num == 1:
        pass
    print("Number:", num)
print('\n')

"""4.Mini Project: Number Guessing Game
goal:
+Generate a random number between 1 and 10
+ Ask the user to guess it 
+ Give hints: "Too high" or "Too low"
+ End when guessed correctly"""
# traduccion
"""4. Miniproyecto: Juego de adivinanzas de números
Objetivo:
+ Generar un número aleatorio entre el 1 y el 10
+ Pedir al usuario que lo adivine
+ Dar pistas: "Demasiado alto" o "Demasiado bajo"
+ Terminar cuando se acierta"""

import random

secret = random.randint(1, 10)
guess = None

while guess != secret:
    guess = int(input("Guess a number between 1 and 10:"))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You gussed it!")

