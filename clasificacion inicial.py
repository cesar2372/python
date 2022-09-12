sexo =str(input("ingrese el sexo de el o la estudiante: "))
nombre=str(input("ingrese el nombre de el o la estudiante: "))
if sexo=="femenino" and nombre.capitalize() >  "m":
    group="a"
elif sexo=="masculino" and nombre.capitalize() < "n":
    group="a"
else:
    group="b"
print("el o la estudiante pertenece al grupo",group)