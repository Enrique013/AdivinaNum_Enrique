#adivina_numero
import random
def adivina_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al juego de adivinar el número!")
    print("He elegido un número entre 1 y 100. ¡Intenta adivinarlo!")

    while True:
        try:
            adivinanza = int(input("Introduce tu adivinanza: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print("Demasiado bajo. Inténtalo de nuevo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto. Inténtalo de nuevo.")
            else:
                print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

adivina_numero()