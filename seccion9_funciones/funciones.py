print("***************parametro opcional")
def persona(nombre,edad=None):
    print(f"te llamas {nombre}")
    if(edad):
        print(f"Y tienes {edad} años")

persona("Marlon")
persona("Marlon",22)

print("\n\n***************funciones return")
def isOdd(numero):
    return numero%2

print(f"¿el numero 3 es impar? {bool(isOdd(3))}")

print("\n\n***************funciones lambda")
cuadrado = lambda num: f"el cuadrado de {num} es {num**2}"
print(cuadrado(10))
#ejm 2
enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x : x ** 2, enteros))
print(cuadrados)
#ejm 3
valores = range(1,10)
pares = list(filter(lambda x : not(x % 2), valores))
print(pares)


