nombres = []
i = 0
while i < 5:
    nombre = input("ingresa un nombre: ")
    nombres.append(nombre.upper())
    i=i+1
for nombre in nombres:
    print(nombre)  