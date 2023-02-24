
archivo = open("numbers.txt","r")
lineas = archivo.readlines()
primera_linea = lineas[0]
string = "Juan,Maria,Pedro,Fulano"
string_split = string.split(',')
print(string_split)

primera_linea.split(',')
print(primera_linea.replace('\n',''))
for línea in lineas:
    print(línea)
archivo.close()

archivo = open("numbers.txt","w")
archivo.write("Otra cosa")
archivo.close()

archivo = open("numbers.txt","a")
archivo.write("\nNew line 02\n")
archivo.close()