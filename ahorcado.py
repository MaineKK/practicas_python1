import random

def elegir_palabra():
    palabras = ["gorro", "turron", "isla", "mar"]
    return random.choice(palabras)

def palabra_secreta(palabra, letras_adivinadas):
    return " ".join(letra if letra in letras_adivinadas else "_" for letra in palabra)

def pedir_letra(letras_ingresadas):
    while True:
        letra = input("\nIngresa una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("por favor, ingresa una sola letra válida.")
        elif letra in letras_ingresadas:
            print("Ya ingresastre esa letra. Intenta con otra.")
        else:
            return letra
def jugar():
    palabra_oculta = elegir_palabra()
    letras_correctas = set()
    letras_incorrectas =set()
    vidas = 5
    
    print("\n¡Bienvenido al Ahorcado!")
    
    while vidas > 0:
        print("\nPalabra:", palabra_secreta(palabra_oculta, letras_correctas))
        print(f"letras_incorrectas: {', '.join(letras_incorrectas)}")
        print(f"Vidas restantes: {vidas}")
        
        letra = pedir_letra(letras_correctas | letras_incorrectas)
        
        if letra in palabra_oculta.lower():
            print("correcto!")
            letras_correctas.add(letra)
            
        else:
            print("Incorrecto!")
            letras_incorrectas.add(letra)
            vidas -= 1
            
        if set(palabra_oculta) <= letras_correctas:
            print("\nFelicidades! has adivinado la palabra:", palabra_oculta)
            return
        
    print(f"\nPerdiste, la palabra era '{palabra_oculta}")

jugar()