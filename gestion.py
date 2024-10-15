import os

# Lista para almacenar los productos
productos = []

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio} - Cantidad: {self.cantidad}"

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    cantidad = int(input("Introduce la cantidad del producto: "))
    producto = Producto(nombre, precio, cantidad)
    productos.append(producto)
    print("Producto añadido con éxito.")

def ver_productos():
    if not productos:
        print("No hay productos en el inventario.")
    else:
        print("Productos en el inventario:")
        for producto in productos:
            print(producto)

def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto.nombre == nombre:
            nuevo_nombre = input("Introduce el nuevo nombre del producto (o presiona Enter para mantener el actual): ")
            if nuevo_nombre:
                producto.nombre = nuevo_nombre

            nuevo_precio = input("Introduce el nuevo precio del producto (o presiona Enter para mantener el actual): ")
            if nuevo_precio:
                producto.precio = float(nuevo_precio)

            nueva_cantidad = input("Introduce la nueva cantidad del producto (o presiona Enter para mantener la actual): ")
            if nueva_cantidad:
                producto.cantidad = int(nueva_cantidad)

            print("Producto actualizado con éxito.")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for producto in productos:
        if producto.nombre == nombre:
            productos.remove(producto)
            print("Producto eliminado con éxito.")
            return
    print("Producto no encontrado.")

def guardar_datos():
    with open("productos.txt", 'w') as file:
        for producto in productos:
            file.write(f"{producto.nombre},{producto.precio},{producto.cantidad}\n")
    print("Datos guardados con éxito.")

def cargar_datos():
    if os.path.exists("productos.txt"):
        with open("productos.txt", 'r') as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(',')
                productos.append(Producto(nombre, float(precio), int(cantidad)))
        print("Datos cargados con éxito.")
    else:
        print("No se encontró el archivo de datos.")

def menu():
    cargar_datos()  # Cargar los datos al inicio
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Ejecutar el menú principal
menu()
