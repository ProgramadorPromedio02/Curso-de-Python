class Gato:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def maullar(self):
        print("Miau!")

mi_gato = Gato("Pelusa", 5)
mi_gato.maullar() # Output: Guau!
