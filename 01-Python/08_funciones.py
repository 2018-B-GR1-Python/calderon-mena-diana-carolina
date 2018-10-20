def hola_mundo(): # funciones sin return retorna none
    print('hola mundo')


hola_mundo()


def sumar_dos_numeros(num_uno, num_dos):
    if(num_uno == 1):
        return "hola"
    else:
        return num_dos + num_uno


print(sumar_dos_numeros(1,9))


def imprimir_universidad(nombre_universidad = "EPN"):
    print(f"nombre de la universidad: {nombre_universidad}")


imprimir_universidad()
imprimir_universidad("salford")


def guardar_carros(posicion, placa, usuario, tipo, color):
    print(f"Guardamos en el {posicion} en el auto con placa {placa} del {usuario} ")
    if(color):
        print(f"se recibio un tipo de {color}")
    if(tipo):
        print(f"el auto es de tipo {tipo}")


guardar_carros(1, "123-SSD", "CAROLINA", tipo=333, color="verde")
guardar_carros(tipo=333, color="verde", posicion=1, placa="123-SSD", usuario="CAROLINA")


# por defecto
# normales
# *

def sumar_n_numeros(resta, *numeros, valor_inicial=0):
    for numero in numeros:
        valor_inicial = valor_inicial+numero
    return valor_inicial - resta


resultado = sumar_n_numeros(1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, valor_inicial=10)

print(resultado)


def imprimir_nombre(**kwargs): ## key word arguments
    print(f"{kwargs['primer_nombre']} {kwargs['segundo_nombre']} "
          f"{kwargs['apellido_materno']} {kwargs['apellido_paterno']}")


imprimir_nombre(primer_nombre="Diana", segundo_nombre="Carolina",
                apellido_materno="Mena", apellido_paterno="Calderon")

#nombre = input("Ingrese su nombre ")
#print(nombre)

#numero = input("Ingrese un numero")
#print(int(numero) + 1)

#opcional = input("Desea papas con su orden?? Si o No")

#if (True if opcional == "Si" else False):
 #   print("Truty")
#else:
 #   print("Falsy")


#number = input("Ingrese los numeros")

#number = number.split(",")

#print(sumar_dos_numeros(int(number[0]), int(number[1])))

def calculadora(numero_uno, numero_dos, operacion= "suma"):
    def sumar_dos_numeros():
        return numero_uno + numero_dos
    def restar_dos_numeros():
        return numero_uno - numero_dos
    def dividir():
        return numero_uno/numero_dos
    def multiplicar():
        return numero_uno*numero_dos
    def switch_operaciones():
        return {
        'suma':sumar_dos_numeros(),
        'resta': restar_dos_numeros(),
        'dividir': dividir(),
        'multiplicar': multiplicar()
    }[operacion]
    return switch_operaciones()


print(calculadora(10, 5, "dividir"))


def leer_archivo(path):
    try:
        archivo_abierto = open(path)  # por defecto es la r -> read
        arreglo_lineas = archivo_abierto.readlines()
        for linea in arreglo_lineas:
            print(linea)
        archivo_abierto.close()
    except Exception:
        print("No se pudo leer")


def agregar_a_archivo(path, *lineas_a_escribir):
    try:
        archivo_abierto = open(path, "a")  # por defecto es la r -> read
        for linea in lineas_a_escribir:
            archivo_abierto.write("\n"+linea)

        archivo_abierto.close()
    except Exception:
        print("No se pudo leer")


agregar_a_archivo('./08_archivo.txt', "hola", "esta", "bien")
leer_archivo('./08_archivo.txt')