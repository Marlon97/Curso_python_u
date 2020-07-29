numero1 = int(input("ingresa el primer numero: "))
numero2 = int(input("ingresa el segundo numero: "))

if numero2<numero1:
    print("el numero 1 debe ser menor al numero 2")
else:
    for i in range(numero1,numero2+1):
        print(i)