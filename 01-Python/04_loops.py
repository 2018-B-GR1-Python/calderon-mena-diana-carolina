arregloNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in arregloNumeros:
    print(numero)

for x in range(0, 5):
    print(f"Numero de intereacion {x}")

print("/")
for indice in range(3):
    print(f"Numero de intereacion {indice}")
print("/")

for x in range(7, 10):
    print(f"Numero de intereacion {x}")

print("/")

for indice in range(10):
    print(f"Numero de intereacion {indice}")
    if (indice == 6):
        break #  se detiene la ejecucion

print(" /")

for indice in range(10):
    if (indice == 6 or indice == 4):
        continue #  se detiene la ejecucion de esta interacion y el loop continua
    print(f"Numero de intereacion {indice}")


numeroAuxiliar = 0

while numeroAuxiliar < 10:
    print(f"Numero : {numeroAuxiliar}")
    numeroAuxiliar += 1

numeroAuxiliar2 = 0

while True:
    print(f"Numero : {numeroAuxiliar2}")
    numeroAuxiliar2 += 1
    if numeroAuxiliar2 == 20:
        break
