# DICCIONARIO:
menu = {
    "avena": 10.00,
    "leche": 23.00
}

menu["pan"] = 500.00 # ASIGNANDO NUEVO ITEM AL DICCIONARIO
print(menu["avena"]) # PRINTEANDO ITEM PUNTUAL

# RECORRIENDO LAS CLAVES DE UN DICCIONARIO:
for key in menu:
    print(key)

# RECORRIENDO CLAVES Y VALORES DE UN DICCIONARIO:
for key, value in menu.items():
    print(key)
    print(value)

# TUPLAS:
tupla = ('juan', 'pedro', 'pedro')
tupla[1] # PODEMOS ACCEDER A LOS ITEMS DE UNA TUPLA IGUAL QUE COMO CON LAS LISTAS
nueva_lista = list(tupla) # CONVERTIR TUPLA A LISTA
print(nueva_lista)
nueva_lista[1] = 'otro pedro'
print(nueva_lista)
print(tupla)

# SETS
my_set = {'test', 23, False}
nueva_lista = list(my_set) # CONVERTIR SET A LISTA
nuevo_set = set(tupla) # CONVERTIR TUPLA A SET
final_lista = list(nuevo_set) # CONVERTIR SET A LISTA

my_list = ['hola', 'test', 34]
nueva_tupla = tuple(my_list) #CONVERTIR LISTA A TUPLA
print(nueva_tupla)