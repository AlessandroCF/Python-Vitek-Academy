# listas, tuplas y funciones

#listas
'''
frutas = ["Sandia", "Banano", "Fresa"]
print("Primer print", frutas)

frutas.append("Manzana")
frutas.append("Uva")
print("Primer print", frutas)

#frutas.remove("Banano")
frutas.remove(frutas[1])
print("Primer print", frutas)
print(f"Primer print {frutas}")
print(f"Elemento 3 {frutas[2]}")

for fruta in frutas:
    print(f'Frutas: {fruta}')

'''

#tuplas
'''
colores = ("rojo", "azul", "blanco")
#colores[0] = "morado" error
print(colores)
'''

#dicionarios
'''
persona = {
    "nombre" : "Alessandro",
    "edad" : 59,
    "ciudad" : "Tres Rios",
    "profesion" : "ingeniero"

}

print(persona)
print(f"Nombre del cliente:  {persona["nombre"]}")
print(f"Eda del cliente:  {persona["edad"]}")
persona["estado civil"] = "casado"
print(persona)
del persona["ciudad"]
print(persona)

#listas de dicionarios:
#personas = [persona1, persona2]

'''
#metodos o funciones

def saludar(nombre):
    print("Hola", nombre)

saludar("Bertha")    

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

print(suma(5, 2))

resultadoSuma = suma(7, 9)
print(resultadoSuma)

