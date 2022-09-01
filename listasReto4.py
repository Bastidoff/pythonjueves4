numeros=[]
#numeros=[1,2,20,56,23,89,12,6,4,32,154,89,54,84,28,65,36,21,32,874]
for i in range(20):    
    numeros.append(int(input("Ingrese un número: ")))
    
print(numeros)

numeroBusqueda=int(input("Ingrese el número que desea buscar: "))

if numeroBusqueda in numeros:
    print(f'¡Bravo! El número {numeroBusqueda} sí se encuentra en la lista. ')
else:
    print(f'¡OH! El número {numeroBusqueda} NO se encuentra en la lista.' )