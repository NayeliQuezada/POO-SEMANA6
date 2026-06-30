# Clase padre Producto

class Producto:

    def __init__(self, nombre, precio, disponibilidad):
        self.nombre = nombre
        self.__precio = precio
        self.disponibilidad = disponibilidad

    # Método getter
    def obtener_precio(self):
        return self.__precio

    # Método setter con validación
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio debe ser mayor que cero.")

    # Método que será sobrescrito
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.__precio}")
        print(f"Disponible: {self.disponibilidad}")