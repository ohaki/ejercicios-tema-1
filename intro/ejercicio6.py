cadena = "zeréP nauJ,01"
nombre_apellido = cadena[::-1].split(',')[0][::-1]
nota = cadena[::-1].split(',')[1][::-1]
resultado = f"{nombre_apellido} ha sacado un Nota de {nota}."
print(resultado)