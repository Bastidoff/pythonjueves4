#construir un programa que reciba números enteros y los vaya sumando, se digita un número negativo debe terminar

numero=0
suma=0
while(numero>=0):
    
    numero=int(input("Ingrese un número positivo para sumar: "))
    if(numero>=0):
        suma=suma+numero
    else:
        break

print(f'La suma de los número positivos ingresados es: {suma}')