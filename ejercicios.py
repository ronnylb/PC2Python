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