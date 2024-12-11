# preguntar al usuario nombre y decir he pensao un numero entre 1 y 100 y tienes 8 intentos. 
# 1 si es imenor a 1 o superior a 100 no esta permitido, si es menor es incorrecto, si es mayor tmb es incorrecto,
# si acerto se dice que gano y los intento que hizo. y se repite hasta que gane o hasta que se agoten los intentos.

from random import *

jugador = input("ingresa tu nombre? ")

aleatorio = randint(1,100)

print(f"Hola {jugador}, he pensado un numero del 1 al 100 y tienes 8 intentos para adivinarlo.")

intentos = 8

for intento in range(1, intentos +1):
    try:
        juego = int(input(f"intento {intento}: cual crees que es el número?"))
        
        if juego < 1 or juego > 100:
            print("Error: el numero no valido.")
            continue
        if juego > aleatorio:
            print("incorrecto, el numero ganador es menor")
        elif juego < aleatorio:
            print("incorrecto, el numero ganador es mayor")
        else:
            print(f"Correcto, {jugador}! has adivinado en el intento {intento}.")
            break
    except ValueError:
        print("Por favor, introduce un numero valido.")
        
else:
    print(f"Lo siento, se acabaron los intentos. El numero era {aleatorio}!")
    
   