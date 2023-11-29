# PRACTICA 2

#Estructuras Iterativas

#Problema 1

    def numeros_divisibles_multiplos(limite_inferior, limite_superior):
    if limite_superior>limite_inferior:
        resultado=[]   
        for n in range(limite_inferior,limite_superior):
            n+=1
            if n%7==0 and n%5==0:
                resultado.append(n)
        return resultado
    else:
        print("El limite inferior debe ser menor al limite superior")

#Problema 2

n=5

for i in range(1,n+1):
    for j in range(i):
        print("* ",end="")
    print()

for i in range(n-1,0,-1):
    for j in range(i):
        print("* ",end="")
    print()

#Problema 3

totalpares=0
totalimpares=0
totalnumeros=list()

while True:
    pregunta=str(input("Desea ingresar un número?"))
    if pregunta=='SI' or pregunta=='si':
        numero=int(input("“Ingrese el número: "))
        totalnumeros.append(numero)
        pares=0
        impares=0
        if numero%2==0:
            pares+=1
            totalpares+=1
        else:
            impares+=1
            totalimpares+=1
    else:
        pregunta=='NO' or pregunta=='no'
        break
    
print("Cantidad de números ingresados:",totalnumeros)
print("Cantidad de números pares:",totalpares)
print("Cantidad de números impares:",totalimpares)

#Problema 4
alumnos = []
while True:
    alumno = {}
    alumno["Alumno"] = input("Ingrese el nombre del alumno (o 'q' para salir): ")  
    if alumno["Alumno"] == "q":
        break
    notas = []
    notas.append(int(input("Ingrese la primera calificación: ")))
    notas.append(int(input("Ingrese la segunda calificación: ")))
    notas.append(int(input("Ingrese la tercera calificación: ")))
    alumno["Notas"] = notas
    alumnos.append(alumno)
print("Listado de alumnos:")
for alumno in alumnos:
    print("Alumno:", alumno["Alumno"])
    print("Notas:", alumno["Notas"])
    print()

#Problema 5
def contar_digitos(numero, digito):
    numero_str = str(numero)
    cantidad = numero_str.count(str(digito))
    return cantidad
numero = 15789000
digito = 0
cantidad = contar_digitos(numero, digito)
print(f"Cantidad de veces {digito} en el número: {cantidad}")

#Problema 6
def fibonacci(limite):
    num1 = 0
    num2 = 1
    print(num1)
    print(num2)
    while num2 < limite:
        siguiente = num1 + num2
        print(siguiente)
        num1 = num2
        num2 = siguiente

fibonacci(50)

#Problema 7
def es_primo(numero):
    if numero <= 1:
        return print("No es primo")
    for i in range(2, numero):
        if numero % i == 0:
            return print("No es primo")
    return print("Es primo")

#Problema 8
def facto_numero(num):
    r=1
    for i in range(num):
        i+=1
        r*=i
    return r

n=int(input("Ingrese el numero"))
resultado=facto_numero(n)
print("El numero factorial es: ",resultado)

#Problema 9



