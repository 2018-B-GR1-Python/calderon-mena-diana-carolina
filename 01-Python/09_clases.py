class Escuela:

   # valorCategoria = 4
    pais = 'Ecuador'  # atributo publico
    __cuidad = 'quito'  # atributo privado, tambien sirve para funciones

    def __init__(self, nombre, valor_categoria=4):
        print(self)
        print("hola")
        self.nombre = nombre
        self.valor_categoria = valor_categoria

    def saludar(self):
        print(f'hola desde {self.nombre} localizada en {self.cuidad} - {self.pais}' )

    def categoria(self):
        return self.valorCategoria * 3

    def __str__(self):
       return 'Escuela'


#t = Escuela('EPN ')
#t.valorCategoria = 2
#t.saludar()
#print(t.categoria())


class Auto:

    __ensamblado = 'Quito'
    numero_asientos = 5

    def __init__(self, nombre, color, color_techo):
        self.nombre = nombre
        self.color = color
        self.color_techo = color_techo

    def cambiar_ensamblado (self, ensamblado):
        self.__ensamblado = ensamblado

    def __maximo_numero_pasajeros(self):
        return self.numero_asientos+3

    def __str__(self):
        return f' {self.color} - {self.nombre} - {self.__ensamblado} - {self.numero_asientos}' \
               f'- {self.__maximo_numero_pasajeros()} - {self.color_techo} '


bm = Auto('mazda', 'negro', 'cafe')


print(bm)


class Hyundai (Auto):

    def __init__(self, color, nombre):
        super().__init__(nombre=nombre, color=color, color_techo='azul')
        print('constructor')
        print(self.nombre)


mi_carro = Hyundai('negro', 'aa')
print(mi_carro)