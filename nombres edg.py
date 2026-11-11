nombres=["Angel","mi edgar","adrian","el husky","makako"]
print(f"Los nombres que se tienen son:{nombres}")
nombreBuscar=input("¿Que nombre deseas buscar?:")
encontrado=False
contador=0
i=0
while i<len(nombres):
    if nombres[i]==nombreBuscar:
        encontrado=True
        contador=contador+1
        print("Encontrado en la posicion:",i)
        i=1+1
if encontrado==True:
    print("Nombre encontrado")
    print("Aparece",contador,"veces")
else:
    print("Nombre no encontrado")
