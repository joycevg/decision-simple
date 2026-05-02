"""
    Ejemplo de estructura de condicional
    simple actualizado
"""
# variable edad, asume el valor ingresado porteclado
edad = input("Ingrese la edad de la persona: ")

# la variable edad, asume un valor de tipo cadena
# por defecto con la función input
# Se debe hacer un cambio de tipo de dato para que
# sea considerado con entero, a través de int

edad = int(edad)

# desde aquí la variable edad es considerada con tipo d
# de dato entero

if edad >= 18:
    print("La persona es mayor de edad en Ecuador")


