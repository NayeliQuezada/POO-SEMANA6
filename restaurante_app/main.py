from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante()

# Platillos de parrillada
platillo1 = Platillo(
    "Parrillada Mixta",
    18.50,
    True,
    1200
)

platillo2 = Platillo(
    "Costillas BBQ",
    15.75,
    True,
    950
)

# Bebidas
bebida1 = Bebida(
    "Limonada Natural",
    2.50,
    True,
    500
)

bebida2 = Bebida(
    "Té Helado",
    2.00,
    True,
    450
)

# Prueba de encapsulación
print("Precio original de la Parrillada Mixta:")
print(platillo1.obtener_precio())

platillo1.cambiar_precio(19.50)

print("Nuevo precio:")
print(platillo1.obtener_precio())

# Agregar productos
restaurante.agregar_producto(platillo1)
restaurante.agregar_producto(platillo2)
restaurante.agregar_producto(bebida1)
restaurante.agregar_producto(bebida2)

# Mostrar productos
restaurante.mostrar_productos()