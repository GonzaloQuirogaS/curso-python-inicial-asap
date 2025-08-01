'''
    Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces 
    aparecen todas las vocales considerando minúsculas, mayúsculas y acentos.
'''

oracion = input("Ingrese una oracion: ")
a = 0
e = 0
i = 0
o = 0
u=  0

for letra in oracion:
    if letra in "aáAÁ":
        a = a + 1
    elif letra in "eéEÉ":
        e = e + 1
    elif letra in "iíIÍ":
        i = i + 1
    elif letra in "oóOÓ":
        o = o + 1
    elif letra in "uúUÚ":
        u = u + 1

print(f"La oracion '{oracion}' tiene:")
print(f" - {a} letras 'a'")
print(f" - {e} letras 'e'")
print(f" - {i} letras 'i'")
print(f" - {o} letras 'o'")
print(f" - {u} letras 'u'")