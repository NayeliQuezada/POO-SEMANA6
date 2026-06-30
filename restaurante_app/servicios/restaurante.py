class Restaurante:
    
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("\nLISTA DE PRODUCTOS")
        print("-" * 30)

        for producto in self.productos:
            producto.mostrar_informacion()
            print("-" * 30)