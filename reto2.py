'''
Codificar un programa que presente un menú de 4 opciones y reciba un numero natural  para realizar las siguientes operaciones:
	
	0: Salida
	1: Encuentre si el número es múltiplo de 2
	2: Encuentre la raíz cuadrada del número
   	3: Sume 100 al número ingresado
 	4: Eleve a la 2 el número ingresado
'''
import math

opcion=1
numero=int(input("Ingrese un número natural: "))
print("************MENÚ************")
print("0: Salir")
print("1. Saber si el número es múltiplo de 2")
print("2. Saber la raíz cuadrada del número")
print("3. Sumar 100 al número ingresado")
print("4. Elevar a la 2 el número ingresado")
while opcion!=0:    
    opcion=int(input("Ingrese una opción: "))
    
    if opcion==1:
        if numero%2==0:
            print(f"El número ingresado ({numero}) es múltiplo de 2")
        else:
            print(f"El número ingresado ({numero}) NO es múltiplo de 2")
    elif opcion==2:
        raiz=math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es {raiz}")
    elif opcion==3:
        suma=numero+100
        print(f"{numero} + 100 = {suma}")
    elif opcion==4:
        cuadrado=numero**2
        print(f"{numero} elevado a la 2 es {cuadrado}")
    elif opcion==0:
        break
    else:
        print("Ingrese una opción válida.")
    
