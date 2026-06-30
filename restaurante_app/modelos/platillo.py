from modelos.producto import Producto

# Clase hija Platillo

class Platillo(Producto):

    def __init__(self, nombre, precio, disponibilidad, calorias):
        
        super().__init__(nombre, precio, disponibilidad)
        self.calorias = calorias

    # Polimorfismo
    def mostrar_informacion(self):
        print("----- PLATILLO -----")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.obtener_precio()}")
        print(f"Disponible: {self.disponibilidad}")
        print(f"Calorías: {self.calorias}")
