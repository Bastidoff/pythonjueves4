ciudades=[]

for i in range(8):
    ciudades.append(input("Ingrese una ciudad colombiana: "))

print(f'Orden original: {ciudades}')

inversa=list(reversed(ciudades))

print(f'Orden inverso: {inversa}') 