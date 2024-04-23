# variables

contador = 0
print(contador)

contador += 1
contador += 1

print(contador)

# Tipado dinamico
contador = "Hola"
print(contador)

# estructuras de control
condicion = False #True # False

if condicion:
    print("La condicion es verdadera")

else:
    print("La condicion es falsa")

for i in range(0, 10):
    print(i)

lista = ["Hola", "Si", "Adios"]

for palabra in lista:
    print(palabra)


condicion = True

contador = 0
while condicion:
    contador += 1
    print(contador)

    if contador > 12:
        break

print("Adios")