'''
    Suponga que tiene una verdulería y carga la cantidad y el precio de lo comprado por un cliente. 
    Realice un programa que tome de a uno la cantidad y el precio comprado por el cliente 
    y al finalizar la compra retorne el monto total gastado. 
'''

total = 0

print("------ Facturacion de verduleria | Ingrese 0 para salir ------")
while True:
    cantidad = int(input("Ingrese la cantidad a comprar (en kg o unidad): "))
    if cantidad == 0:
        break
    precio = float(input("Ingrese el precio por unidad o kg: "))
    
    subtotal = cantidad * precio
    total += subtotal
    print(f"Subtotal: ${subtotal:.2f}")

print(f"\nMonto total gastado: ${total:.2f}")