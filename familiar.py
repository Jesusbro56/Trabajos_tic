print("PROGRAMA DE APOYO FAMILIAR")
sexo = input("Ingresar sexo")
edad = int(input("Ingresar edad"))
estadoCivil = input("ingrese estado civil (soltero/casado): ").lower()
hijos = int(input("cantidad de hijos"))

if sexo == "mujer" and hijos == 1 and edad < 18:
    print("Eres mujer , tienes un hijo y eres menor de edad.")
    print("El apoyo sera de 800")
elif sexo == "mujer" and hijos == 1 and edad >= 18:
    print("Eres mujer , tienes un hijo y eres mayor de edad.")
    print("El apoyo sera de 300")
elif sexo == "mujer" and hijos < 1 and edad < 18:
    print("Eres mujer , tienes mas de un hijo y eres menor de edad.")
    print("El apoyo sera de 1500")
elif sexo == "mujer" and hijos > 1 and edad >= 18:
    print("Eres mujer , tienes mas de un hijo y eres mayor de edad.")
    print("El apoyo sera de 500")
elif sexo == "hombre" and hijos >= 1 and estadoCivil == "soltero":
       print("eres hombre y tienes hijos.")
       print("El apoyo es de 780")
else:
     print("no valido")