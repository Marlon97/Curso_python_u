numero = int(input("ingresa la cantidad de numeros a sumar: "))
suma=0
for i in range (1,numero+1):
    suma += int(input("ingresa un numero: "))
print(f"La suma es: {suma}")