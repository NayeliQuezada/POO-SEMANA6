from modelos.producto import Producto

class Bebida(Producto):
    
    def __init__(self, nombre, precio, disponibilidad, volumen):
        super().__init__(nombre, precio, disponibilidad)
        self.volumen = volumen

    def mostrar_informacion(self):
        print("=== BEBIDA ===")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio()}")
        print(f"Disponible: {self.disponibilidad}")
        print(f"Volumen: {self.volumen} ml")