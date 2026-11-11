numeros=[]
resultados=[]
i=0
while i <5:
    num=int(input("ingresa un numero:"))
    numeros.append(num)
    i=i+1
multiplicador=int(input("¿por cuanto deseas multiplicar?:"))

for num in numeros:
    resultado=num * multiplicador
    resultados.append(resultado)

print("Numeros originales:", numeros)
print("Resultados:", resultados)
