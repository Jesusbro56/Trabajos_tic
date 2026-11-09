#Programa que
#Ponerle nombre a mi lista
peliculas=[]
#Preguntar cuantas pelis
cantidadPelis=int(input("cuantas peliculas vas a agregar"))
i=0
#Mientras1 sea menor a cantidad ejecutada
while i<cantidadPelis:
    #preguntar peliculas
    peli=input("ingresa peli: ")
    peliculas.append(peli)
    print("Peliculas")
    i=i+1
#Buscar una pelicula en la lista
# #Preguntar la peli a buscar
peliBuscar=input("Que peli buscas")    
if peliBuscar in peliculas:
    print("Si esta")
else:
    print("No esta pero dejame la agrego")
    peliculas.append(peliBuscar)
    print(peliculas)    