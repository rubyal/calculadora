print("SE INICIA PROGRAMA")
entrada=input().split(" ")
entrada2=list(map(int,entrada))
print(entrada2)
hasta=34
numero=0
suma=0
while(numero<=hasta):
    numero=numero+1
    suma+=entrada2[numero-1]
print(suma)