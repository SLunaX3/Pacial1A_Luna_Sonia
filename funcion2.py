def reemplazarCaracteres(cadena, caracter_original, caracter_reemplazo):
    cantidad_reemplazos = cadena.count(caracter_original)
    cadena_reemplazada = cadena.replace(caracter_original, caracter_reemplazo)
    return cantidad_reemplazos, cadena_reemplazada    

# main

cadena = input("Ingrese una cadena de caracteres: ")
caracter_original = input("Ingrese el carácter a reemplazar: ")
caracter_reemplazo = input("Ingrese el carácter de reemplazo: ")

cantidad_reemplazos, cadena_reemplazada = reemplazarCaracteres(cadena, caracter_original, caracter_reemplazo)

print("Cantidad de reemplazos realizados:", cantidad_reemplazos)
print("Cadena con reemplazos:", cadena_reemplazada)