nombre = input("por favor, dime tu nombre: ")
ventas = input("diga sus ventas totales del mes: ")

ventas = int(ventas)



comision = ventas * 13 / 100

comision = round(comision, 2)

print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")