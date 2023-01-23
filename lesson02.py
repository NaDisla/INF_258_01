# Listas:
cosas = ["carro", False, 45.2, 452, ["Hola", False]]

# Lista dinámica:
cantidad = int(input("Ingrese la cantidad de elementos: "))
nueva_lista = []
for i in range(cantidad):
    dato = input("Ingrese un dato: ")
    nueva_lista.append(dato)
print(nueva_lista)

# Insertar item en posición específica:
nueva_lista.insert(3,"Nuevo item")
print(nueva_lista)

#FOR anidados:
for c in cosas:
    print(c)
    for i in cosas[4]:
        print(i)

# Recorrer cadenas:
string = "test"
for s in string:
    print(s)

# Recorrer rango:
for i in range(12):
    print(i)

# Número aleatorio:
import random
for i in range(5):
    nuevo_numero = random.randint(1001,9999)
    print(nuevo_numero)

# Caracteres especiales
string = "Cualquier cosa\n"
print(string)
print("Testestomuchomaslargo\t\t\t\t\t\thola")
