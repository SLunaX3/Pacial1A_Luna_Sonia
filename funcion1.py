
def aplicarAumento(precio_producto):
    aumento = precio_producto * 0.05
    precio_con_aumento = precio_producto + aumento
    return precio_con_aumento

# main

precio_producto = float(input("Ingrese el precio del producto: "))
precio_con_aumento = aplicarAumento(precio_producto)
print("El valor del producto con un aumento del 5%: ", precio_con_aumento)