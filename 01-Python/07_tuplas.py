tupla = (1, 2, 3, 2, 3, 3, "a", False, "a", "a")
print(tupla)

for numeros in tupla:
    print(f"numero: {numeros}")

print(tupla.index(1))  # index of
print(tupla.count(3))  # devuelve el numero de repeticiones del valor

print(tupla[-1])
print(tupla[0:2])

#  No se puede añadir elementos a una tupla
#  Las tuplas son fijas

# Obtener la tupla sin los repetidos
print(set(tupla))

for valor in set(tupla):
    print(f"valor: {valor}")

arreglo = [1, 2, 3]
arregloDos = [4, 5, 6]
print(arreglo + arregloDos)

arregloUno = [[1,2], [2,3]]
arregloDoss = [[4,6], [3,3]]
print(arregloUno + arregloDoss)
