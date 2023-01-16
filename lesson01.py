
edad = int(input('Introduzca su edad: ')) # Captura por teclado número entero
sueldo = float(input('Introduzca su sueldo: ')) # Captura por teclado número decimal
sueldo_redondeado = round(84.55333322556,2) # Redondeo
print(sueldo_redondeado) # Impresión de variable 

# **************** Concatenación e interpolación de variables ****************
print("Su edad es: " + str(edad) + " y su nombre es fulano")
print(f"Su edad es: {edad}")
print("Su edad es: {otra}".format(otra=edad))
print("La temperatura X en °F es fkkvk:", edad)

# **************** Condiciones, operadores de comparación y lógicos ****************
if edad > 0 and edad < 40:
    print("Estás vivo")
elif edad >= 50 and edad <= 80:
    print("Eres medio viejo")
elif edad >= 90 or edad == 100:
    print("Te estás casi muriendo")
else:
    print("Moriste")