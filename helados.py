ice_cream=1000
print("............menu.................")
print("1-topping de oreo.............200")
print("2-topping de kit kat..........300")
print("3-topping de brownie..........350")
print("4-topping de snicker..........400")
print("")
topping=int(input("seleccione la opcion de topping que desea para su helado: "))
if topping==1:
    pt=200
elif topping==2:
    pt=300
elif topping==3:
    pt=350
elif topping==4:
    pt=400
else:
    print("no tenemos el topping seleccionado")
   
print("el precio de su helado es",ice_cream+pt)