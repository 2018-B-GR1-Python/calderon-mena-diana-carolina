print("Hola Mundo")

edad: int = 20
sueldo = 1.02

print(edad + int(sueldo))

nombre = "Carolina"  # Comentarios
apellido = 'Calderon'
apellido_materno = """Mena"""

print(nombre)
print(apellido)
print(apellido_materno)

print(nombre == apellido)  # True / False
print(apellido == apellido_materno)
print(apellido_materno == nombre)

print(int(True))  # 1
print(int(False))  # 0

print(str(True))

# Tipos de funciones con strings

print("carolina calderon".capitalize())  # Primera letra del string mayuscula

nombre_completo = "carolina calderon".split(" ")  # devuelve un arreglo

print(nombre_completo[0].capitalize() + " " + nombre_completo[1].capitalize())
print("caro".isalpha())  # True que sean letras
print("caro10".isalpha())

print("caro22".isnumeric())  # si es numero
print("mm20".isalnum())  # si es alfanumerico

# print(int("casa"))  # error

print("Mi nombre es: {0} {1} ".format(nombre_completo[0].capitalize(), "calderon"))
print(f"Mi nombre es: {nombre_completo[0].capitalize()} {nombre_completo[1].capitalize()}")

print(r"Salto de linea")  # raw para saltos de linea

no_exite = None  # null

print(no_exite)
