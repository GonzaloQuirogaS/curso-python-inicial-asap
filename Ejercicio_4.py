'''
    Escriba un programa que solicite la edad de la persona 
    e imprima todos los años que la persona ha cumplido.
'''

edad = int(input("Ingrese la edad: "))
anios = []

if edad > 0:
    for i in range(1, edad+1):
        anios.append(i)
    print(anios)
else:
    print("Ingrese un numero mayor a 0")       