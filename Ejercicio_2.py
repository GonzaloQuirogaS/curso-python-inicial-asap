'''
    Escriba un programa que consulte al usuario por una oración 
    y comente al usuario cuantas veces aparece la letra “a”. 
'''

oracion = input("Ingrese una oracion: ")
aux = 0
for letra in oracion:
    if letra =="a":
        aux=aux+1

print(f"{oracion} tiene {aux} letras 'a'")