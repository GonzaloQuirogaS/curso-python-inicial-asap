'''
    Tome el ejercicio de cálculo de números pares e impares de la unidad 2 
    y agréguele un bucle al código de forma de simplificarlo.
'''

cantidad=int(input("Ingrese la cantidad de numeros: ")) 

if cantidad > 0:
    for i in range(cantidad):
        numero = int(input(f"Ingrese el número {i + 1}: "))

        if numero % 2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")
else:
    print("Ingrese un numero positivo mayor a 0")