print (print(((3+2)/(2*5))**2))
horas = float(input("Ingrese la cantidad de horas que trabajo: "))
costo_Hora = float(input("ingrese el costo por hora: "))
final= (horas*costo_Hora)
print('uted gana',final)


peso= float(input('ingrese su peso'))
altura = float(input("Ingrese su altura: "))
imc = (peso)/(altura*altura)
print("Tu indice de masa corporal es:",imc)

trompo = 30 #gramos
yoyos = 20 #gramos
cantidad_Trompos = int(input("ingrese la cantidad de trompos que enviara: "))
cantidad_Yoyos = int(input("ingrese la cantidad de yoyos que enviara: "))                  
print("La cantiad de trompos vendida es de:",cantidad_Trompos)
print("La cantidad de yoyos vendida es de:",cantidad_Yoyos)
envio_Trompos = cantidad_Trompos * trompo
envio_Yoyos = cantidad_Yoyos * yoyos
print("El peso del paquete de trompos es de:",envio_Trompos,"G")
print("El peso del paquete de yoyos es de:",envio_Yoyos,"G")
paquete = envio_Trompos + envio_Yoyos
print("El paquete completo pesa:",paquete,"G")

pan = 1000
pan_No_Dia = pan*0.40 #60% de descuento
cantidad = int(input("Ingrese la cantidad de panes que comprara: "))
total = cantidad * pan_No_Dia #cantidad del pan con descuento
               
print("El valor de los panes es de (60% descuento):",total,"Colones")