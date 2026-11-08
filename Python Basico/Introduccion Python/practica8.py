# Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
# Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
import random

secret_number = random.randint(1, 10)

while True:
    number = int(input("Adivine un número del 1 al 10: "))
    if number == secret_number:
        print("¡Felicidades! Has adivinado el número.")
        break
    
    