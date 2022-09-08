edad=int(input('ingrese su edad: '))
ingreso=int(input('ingrese su salario mensual:' ))
impuesto=(ingreso*0.13)
if edad>=16 and ingreso>=125000 :
    print('usted SI debe pagar el impuesto')
    print('por un total de:'); impuesto
else:
    print('usted aun no debe pagar el impuesto')