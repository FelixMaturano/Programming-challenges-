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