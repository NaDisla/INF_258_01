"""
Determinar cantidad de repeticiones de un elemento dado en la siguiente lista:
items = ['fresa', 'cebolla', 'abanico', 'fresa', 23, 84.33, 32, 'cebolla', 23, 23, 'laptop', 'abanico', 84.33]
"""
items = ['fresa', 'cebolla', 'abanico', 'fresa', 23, 84.33, 32, 'cebolla', 23, 23, 'laptop', 'abanico', 84.33]
item_to_search = input("Ingrese un elemento: ")
occurrences = 0

if("." in item_to_search):
    occurrences = items.count(float(item_to_search))
elif(item_to_search.isnumeric()):
    occurrences = items.count(int(item_to_search))
else:
    occurrences = items.count(item_to_search)

if(occurrences > 0):
    print("El elemento %s aparece %s en la lista." % (item_to_search, occurrences))
else:
    print("El elemento %s no se encuentra en la lista." % (item_to_search))

"""
Generar las tablas de multiplicar desde un número N hasta un número M. Cada tabla debe ser hasta el 10.
"""
start = int(input("Ingrese la tabla de inicio: "))
end = int(input("Ingrese la tabla de fin: "))

for i in range(start, end + 1):
    counter = 1
    print("======== TABLA DEL %s ========" % i)
    while counter <= 10:
        result = i * counter
        print("%s x %s = %s" % (i, counter, result))
        counter += 1