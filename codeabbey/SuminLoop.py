print("SE INICIA PROGRAMA")
frutas={"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}
print(frutas)
print("naranja")
frutas["piña"]="pimeapple"
print(frutas)
for clave,valor in frutas.items():
    print("{} en ingles es {}".format(clave,valor))
