edad=int(input('digite la edad de la persona: '))
if(edad<16):
    print('todavia no puede conducir')
elif (edad<18):
    print('puede obtener un permiso para conducir')
elif (edad<70):
    print('puede obtener una licencia estandar')
else:
    print('requiere de una licencia especial')