#ingresar nombre y edad
print("SE INICIA PROGRAMA")
print("ingrese su nombre")
nombre=str(input())
print("ingrese su edad")
edad=int(input())
print("su nombre es {} y tiene {}".format(nombre,edad))
año=str((2021-edad)+100)
print(nombre + "cumplira 100 años en el año" + año)