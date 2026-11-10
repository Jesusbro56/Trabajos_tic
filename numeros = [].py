numeros = []
numPares = []
i=0
while i <10:
    num = int(input("ingresa un numero: "))
    numeros.append(num)
    i = i + 1

for num in numeros:
    if num % 2 == 0:
        numPares.append(num)

print("Numeros pares:")
for num in numPares:
    print(num)
    