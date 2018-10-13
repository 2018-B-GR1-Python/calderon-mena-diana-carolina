import sys

carolina = {
    'nombre': "Carolina",
}
# ctrl + alt + l
try:
    carolina["apellido"]
except KeyError:
    print("Error key")

arregloNumeros = [1, 2]
try:
    arregloNumeros["1"] = 0
    carolina["1"] = 0
except (TypeError, KeyError) as errores:
    print(f"errores {errores}")

except Exception as err:
    print(err.__traceback__)

"""
except TypeError as err:
    print("Error en type")
    print(err.__traceback__.tb_frame)
    print(err.__traceback__.tb_lasti)
    print(f"linea del error {err.__traceback__.tb_lineno}")
"""