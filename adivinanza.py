import random


def juego_adivinanza():
    numero_secreto = random.randint(1, 5)
    intentos = 0
    adivinado = False

    print("Benvenido al juego del calamar")
    print("debes adivinar un numero entre  1 y 100 ")

    while not adivinado:
        adivinanza = input("Introduzca un numero del 1 al 100 ")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor  a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menor a {adivinanza}")
            else:
                print(
                    f"Felicitaciones has ganado el numero  {adivinanza} es el secreto y lo has logrado en {intentos} intentos"
                )
                return

        else:
            print("introduzca un numero valido del 1 al 100")


juego_adivinanza()
