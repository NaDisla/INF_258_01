# WHILE, BREAK, CONTINUE, ACUMULADORES Y CONTADORES
n = 1
suma = 0
while n <= 10:
    x = int(input("Digite el %d número:"%n))
    suma = suma + x
    n = n + 1
print("Suma: %d" % suma)

s = 0
while True:
    v = int(input("Digite un número a sumar o 0 para salir:"))
    if v == 3:
        continue
    elif v == 0:
        break
    s = s + v
print(s)


# Número par/impar
num = int(input("Ingrese número:"))
num_str = str(num)

for s in num_str:
    print(s)

if(num % 2 == 0):
    print("Es par")
else:
    print("Es Impar")