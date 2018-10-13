carolina = {
    'nombre': "Carolina",
    'apellido': 'Calderon',
    'edad': 23,
    'sueldo': 1.02,
    'hijos': [],
    'casado': False,
    'loteria': None,
    "mascota": {
        "nombre": "fuza",
        "edad": 5
    }
}


print(carolina)
print(carolina['nombre'])
print(carolina["mascota"]["nombre"])

print(carolina.get("apellido"))
# eliminar
print(carolina.pop("edad"))
print(carolina)

print(carolina.values())

for valor in carolina.values():
    print(f"El valor es {valor}")

for llave in carolina.keys():
    print(f"La llave es: {llave} valor: {carolina.get(llave)}")

for clave, valor in carolina.items():
    print(f"La llave es: {clave} valor: {valor}")


carolina["profesion"] = "estudiante"
print(carolina)

nuevosValores = {"peso": 0, "altura": 22}
carolina.update(nuevosValores)
print(carolina)

