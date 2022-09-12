edad= int(input("ingrese la edad del cliente: "))
if edad<4 :
    precio="gratis"
elif edad>4 and edad<18 :
    precio=2500
else:
    precio=3000
print("costo es: ",precio)