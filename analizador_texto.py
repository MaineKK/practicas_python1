# Pedir al usuaro que ingrese un texto cualquiera, pedir que tambien ingrese tres letras a eleccion.
# 1. cuantas veces aparece cada una d las letras que ingreso pero hay que convertirlos todos en minuscula.
# 2. cuantas palabras hay a lo largo de todo el texto. con el metodo string para transoformar en una lista y funcion para averiguar el largo
# 3. cual es la primera y ultima letra del texto
# 4. invertir el orden de las palabras.
# 5. ver si la palabra "python" aparece en el texto usando booleano y diccionario.

texto = input("Ingresa un texto a eleccion: ")

texto = texto.lower()

palabras = texto.split()

dic_palabras = {palabra : True for palabra in palabras}
is_python = dic_palabras.get("python", False)
print(f"la palabra 'Python' esta en el texto? {is_python}" )

cantidad_palabras = len(palabras)

print(f"El texto contiene {cantidad_palabras} palabras")

primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra del texto es: '{primera_letra}'")
print(f"La última letra del texto es: '{ultima_letra}'")

texto_reverse = texto[::-1]
print(f"El texto al revés es: '{texto_reverse}'")

dic_palabras = {palabra : True for palabra in palabras}
is_python = dic_palabras.get("python", False)
print(f"la palabra 'Python' esta en el texto? {is_python}" )

letras = input("ahora, ingresa 3 letras aleatorias: ")


letras = letras.replace(" ", "").lower()

if len(letras) == 3:
    print(f"resultado para el texto: '{texto}'")
    for letra in letras:
        print(f"La letra '{letra}' aparece {texto.count(letra)} veces.")
else: 
    print("Por favor, ingresa exactamente 3 letras")
    

palabras = texto.split()

cantidad_palabras = len(palabras)

print(f"El texto contiene {cantidad_palabras} palabras")