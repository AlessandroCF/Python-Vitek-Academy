'''
edad = int(input("Ingrese su edad: "))

if edad >= 65:
    print("Eres adulto mayor")
    print("Dentro del if")

elif edad >= 18:
    print("Eres mayor de edad")
    print("Dentro del elif")

else:
    print("Eres menor de edad")    
    print("Dentro del else")


print("Fuera del if")
'''

'''
for contador in range(6):
    print(contador)

print('----------------')

for contador in range(1, 6):
    print(contador)
    print("segundo for")

for contador in range(3, 10, 3):
    print(contador)

for contador in range(10, 1, -1):
    print(contador)

    
numero = int(input("Ingrese un numero "))    
for contador in rande(1, numero+1):
    print(contador)
'''

'''
numero = int(input("Ingrese un numero "))

while numero >= 1:
    print(numero)
    numero -=1
'''

numero = int(input("Ingrese un numero "))

if (numero <= 0):
    print("Ingrese un numro mayor a 0")
else:
    print("Tablas de multiplicacion")
    for n in range(1, 10+1):
        resultado = numero * n
        print(numero,"x", n, "=", resultado)


