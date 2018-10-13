arreglo = []

arregloNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

arregloCosas = ["a", 2, True, False, 2.3, [1, 2]]

#  intervalo abierto
print(arregloNumeros[0:5])
print(arregloNumeros[3:5])
print(arregloNumeros[:2])
print(arregloNumeros[2:])
print(arregloNumeros[-1])
print(arregloNumeros[-2])
print(arregloNumeros[3:-2])
print(arregloNumeros[-5:-2])

#  Buscar

print(7 in arregloNumeros)
print(15 in arregloNumeros)
print(len(arregloNumeros))

#  Agregar

arregloNumeros.append(10)
print(arregloNumeros)

#  Eliminar
arregloNumeros.pop(-3)
print(arregloNumeros)

arregloNumeros.insert(1, 1.1)
print(arregloNumeros)

del arregloNumeros[1:4]
print(arregloNumeros)
