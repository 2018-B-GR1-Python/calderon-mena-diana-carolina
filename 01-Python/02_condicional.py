# Truthy
# Falsy
if True:
    print("es verdad")
else:
    print("no es verdad")

if False:
    print("es verdad")
else:
    print("no es verdad")

nombre = "Carolina"

if 1 or not 0:  # Es Truthy
    print("si")
else:
    print("no")

if 1 and 0:  # Es Truthy
    print("si")
else:
    print("no")

if "a,b".split(","):  # Es Truthy
    print("si")
else:
    print("no")

# 0 es Falsy
# None, diccionario vacio es Falsy
# numeros truthy excepto el cero

diccionario = []
if diccionario:  # Es Falsy
    print("si")
else:
    print("no")

