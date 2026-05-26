#trabajo final de santiago diaz , ejercicio 2
#Empezamos definiendo una funcion que se encargara de calcular el precio final de cada producto aplicando la promocion si se cumplen las condiciones
def calcularvalorfinal(categoria,preciobase,categoriades,umbral):
    if categoria == categoriades and preciobase > umbral:
        return preciobase * 0.85 #aplica un descuento del 15%, por que 100%-15%=85% osea 0.85
    else:
        return preciobase #si no se cumple la condicion se devuelve el precio base sin descuento
    
#matriz del menu
# cada plato tiene un nombre,categoria,precio base
menu = [
    ["Hamburguesa", "Comida Rapida", 25000],
    ["Pizza", "Comida Rapida", 32000],
    ["Ensalada", "Saludable", 18000],
    ["Pasta", "Italiana", 30000],
    ["Jugo Natural", "Bebida", 12000],
    ["Helado", "Postre", 15000],
    ["Hot dog", "Comida Rapida", 21000],
    ["Sopa", "Saludable", 22000],
    ["Tacos", "Comida Rapida", 28000],
    ["Café", "Bebida", 8000]
]
#datos de la promocion
categoriapromo = "Comida Rapida"
umbralprecio = 20000

print("===== MENÚ DEL RESTAURANTE =====")
print("\nEl dia de hoy tenemos promoción en la categoria de:", categoriapromo)
print("aplica la promoción si el precio es mayor a: $", umbralprecio)

# Recorrer la matriz del menú y calcular el precio final para cada producto
for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]
    #0=nombre, 1=categoria, 2=precio_base con esto accedemos a cada elemento de la matriz para obtener el nombre, categoria y precio base de cada producto

    # con esto calculamos el precio final aplicando la promocion si se cumplen las condiciones
    precio_final = calcularvalorfinal(
        categoria,
        precio_base,
        categoriapromo,
        umbralprecio
    )

    # Mostrar resultados
    print("\nProducto:", nombre)
    print("Categoría:", categoria)
    print("Precio Base: $", precio_base)
    print("Precio Final: $", precio_final)