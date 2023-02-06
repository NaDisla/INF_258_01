# FUNCIONES:

# Función con parámetros requeridos:
def suma(a, b):
    print(a + b)
suma(15, 32) # Llamando la función (ejecutándola)

# Función con parámetros opcionales:
def suma(x, a=10, b=10): # Los parámetros opcionales deben colocarse luego de los parámetros requeridos.
    print(a+b)
    print(x)
suma(15) # La suma será 20 por los parámetros opcionales

# Función de retorno. Este tipo de funciones pueden almacenarse en variables e imprimirse al momento de llamarlas.
def suma_v02(a=15, b=20):
    return a + b
result = suma_v02(15, 32)
print(suma_v02(15, 32))