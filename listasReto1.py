#Construir un programa que reciba el tamaño de una lista  y la llene con múltiplos de 7

multiplos7=[1]
tamano=int(input("Ingrese el tamaño de la lista: "))
for i in range(1, tamano):    
    multiplos7.append(i*7)
    
print(multiplos7)
