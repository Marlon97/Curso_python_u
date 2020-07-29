numero = int(input("ingresa la cantidad de alumnos: "))
aprobados=0
for i in range (1,numero+1):
    if(int(input(f"calificacion del alumno {i}: "))>=70):
        aprobados+=1
print(f"alumnos aprobados: {aprobados}")
print(f"alumnos reprobados: {numero-aprobados}")
