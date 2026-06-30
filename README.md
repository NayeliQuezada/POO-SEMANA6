# Restaurante App

## Autor

Nayeli Quezada

## Descripción

Restaurante App es un sistema desarrollado en Python utilizando Programación Orientada a Objetos. El programa permite registrar productos disponibles en un restaurante y mostrar su información mediante una estructura modular.

## Objetivo

Aplicar los principios fundamentales de la Programación Orientada a Objetos:

- Herencia
- Encapsulación
- Polimorfismo

## Estructura del Proyecto


restaurante_app/
│
├── modelos/
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
│
├── servicios/
│   └── restaurante.py
│
├── main.py
└── README.md


## Herencia

La clase Producto funciona como clase padre.

Las clases Platillo y Bebida heredan los atributos y métodos comunes mediante el uso de la función super().

## Encapsulación

El atributo:

python
__precio


fue encapsulado para impedir modificaciones directas desde fuera de la clase.

Se utilizan los métodos:

python
obtener_precio()
cambiar_precio()


Además se valida que el nuevo precio sea mayor que cero.

## Polimorfismo

Se implementó sobrescribiendo el método:

python
mostrar_informacion()


Cada clase hija muestra información específica según el tipo de producto.

## Productos registrados

### Platillos

- Parrillada Mixta
- Costillas BBQ

### Bebidas

- Limonada Natural
- Té Helado

## Reflexión

La Programación Orientada a Objetos permite organizar mejor los proyectos, reutilizar código mediante herencia, proteger información importante mediante encapsulación y adaptar comportamientos mediante polimorfismo. Estos principios facilitan el mantenimiento y escalabilidad de aplicaciones desarrolladas en Python.