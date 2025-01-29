def devolver_distintos(a, b, c):
    numeros = [a, b, c]
    suma = sum(numeros)

    if suma > 15:
        return max(numeros)
    elif suma < 10:
        return min(numeros)
    else:
        numeros.sort()
        return numeros[1]


print(devolver_distintos(4, 6, 1))


def letras_unicas(palabra):
    return "".join(sorted(set(palabra)))


print(letras_unicas("chanchito"))


def cero_repetido(*args):

    for i in range(1, len(args)):
        if args[i] == 0 and args[i-1] == 0:
            return True
    return False


print(cero_repetido(5, 6, 7, 3, 3, 6, 2, 6, 0))


def contar_primos(n):
    cantidad_primos = 0

    for num in range(2, n + 1):
        es_primo = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i = 0:
                es_primo = False
                break
        
        if es_primo:
            print(num)
            cantidad_primos += 1
            
    return cantidad_primos

resultado = contar_primos(20)
print(f"Cantidad de números primos: {resultado}")