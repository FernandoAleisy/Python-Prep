from cmath import sqrt
import os
from re import T
from tkinter import W
os.system('cls')

def seq(x,y,z=1):
    if x>y:
        y-=1
        z=-int(abs(z))
        return list(range(x,y,z))
    else:
        y+=1
        return list(range(x,y,z))    

## Flujos de Control

print('\n 1. Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero\n')

def com_cero(x):
    if(x<0):
        print('{} es menor a 0'.format(x))
    elif (x>0):
        print('{} es mayor a 0'.format(x))
    else:
        print('{} es igual a 0'.format(x))

com_cero(4)

print('\n  2. Crear dos variables y un condicional que informe si son del mismo tipo de dato\n')

var_1='carro'
var_2=4

if(type(var_1)==type(var_2)):
    print('Las variables son del mismo tipo')
else:
    print('Las variables no son del mismo tipo')


print('\n  3. Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar\n')

for i in seq(1,20):
    if(i%2==0):
        print('{} es par'.format(i))
    else:
        print('{} es impar'.format(i))


print('\n  4. En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3\n')

for i in seq(0,5):
    print(i**3)

print('\n  5. Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos\n')

var_3=7
for i in seq(0,var_3):
    print(i)


print('\n  6. Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0\n')

def factorial(x):
    y=1
    while(x>0):
        y=y*x
        x-=1
    return(y)

print(factorial(4))

print('\n  7. Crear un ciclo for dentro de un ciclo while\n')
i=10
while(i>5):
    for j in seq(i,1,2):
        print('a'*j)
    i-=2

print('\n  8. Crear un ciclo while dentro de un ciclo for\n')

for i in seq(1,20):
    j=i
    while(j%4==0):
        print(j)
        j-=1

print('\n  9. Imprimir los números primos existentes entre 0 y 30\n')

def numeros_primos(x):
    x=int(x)
    if x<2:
        primos=['No hay números primos']
    elif x>2:
        primos=list(range(3,x+1,2))
        primos.insert(0,2)
    else:
        primos=[2]
    
    if len(primos)>4:
        import math
        i=4
        j=1
        while i<len(primos):
            y=int(math.sqrt(primos[i]))
            if primos[i]%primos[j]==0:
                primos.remove(primos[i])
                j=1
            elif primos[j]>=y:
                j=1
                i+=1
            else:
                j+=1
    return(primos)

n=100000
print('Los números primos menores o iguales a', n, 'son: ', str(numeros_primos(n))[1:-1])

print('\n  10. ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin\n')

print('Como esta creado el while, un break es contraproducente, ya que se necesita que dentro del while se evalúe todos los números que estan dentro de una lista. Al aplicar un break se deja de evaluar los siguientes númers. Lo que si óptimiza el tiempo de ejecución es el continue, pero este no afecta las iteraciones del código:\n')

def numeros_primos_o(x):
    ciclos=0
    x=int(x)
    if x<2:
        primos=['No hay números primos']
    elif x>2:
        primos=list(range(3,x+1,2))
        primos.insert(0,2)
    else:
        primos=[2]
    
    if len(primos)>4:
        import math
        i=4
        j=1
        while i<len(primos):
            y=int(math.sqrt(primos[i]))
            if primos[i]%primos[j]==0:
                primos.remove(primos[i])
                j=1
            elif primos[j]>=y:
                j=1
                i+=1
            else:
                j+=1
                continue
    return(primos)

n=30
print('Los números primos menores o iguales a', n, 'son: ', str(numeros_primos_o(n))[1:-1])


print('\n  11. En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?\n')

print('Se puede comparar los codigos utilizando un contador de las iteraciones siempre y cuando la optimización sea utilizando el comando brake. Se crea una variable ciclos=0 y se le suma 1 cada vez que se realzia iteración\n')
print('Cuando solo se utiliza el coando continue, la optimizaión se ve en el tiempo de ejecución del código y cuando la cantidad de iteracciones son bastante grandes\n')

def numeros_primos_o(x):
    ciclos=0
    x=int(x)
    if x<2:
        primos=['No hay números primos']
        ciclos+=1
    elif x>2:
        primos=list(range(3,x+1,2))
        primos.insert(0,2)
        ciclos+=1
    else:
        primos=[2]
        ciclos+=1
    
    if len(primos)>4:
        import math
        i=4
        j=1
        while i<len(primos):
            y=int(math.sqrt(primos[i]))
            if primos[i]%primos[j]==0:
                primos.remove(primos[i])
                j=1
                ciclos+=1
            elif primos[j]>=y:
                j=1
                i+=1
                ciclos+=1
            else:
                j+=1
                ciclos+=1
                continue
    print('con ', ciclos, 'ciclos:')
    return(primos, ciclos)

n=30
print('Los números primos menores o iguales a', n, 'son: ', str(numeros_primos_o(n)[0])[1:-1])


print('\n  12. Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?\n')

print('Si, las fracciones de segundo que no se alcanzan a mostrar se van acumulando, lo que para un número grande como 10000, se nota la diferencia:\n')

n=30
print('Con un promedio de ',numeros_primos_o(n)[1]/n, ' ciclos/número')

n=300
print('Con un promedio de ',numeros_primos_o(n)[1]/n, ' ciclos/número')

n=10000
print('Con un promedio de ',numeros_primos_o(n)[1]/n, ' ciclos/número')


print('\n  13. Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300\n')

i=100
while i>=100 and i<=300:
    if i%12==0:
        print('{} es divisible por 12'.format(i))
        i+=1
    else:
        i+=1
        continue

print('\n  14. Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente\n')

print('Aquí podrás obtener los siguientes números primos despúes de un número dado')
n=int(input('¿Por qué número queires empezar? '))
def siguiente_primo(x):
    if x<2:
        p=2
    elif x==2:
        p=3
    else:
        import math
        primo=False
        x=int(x)
        while primo==False:
            x+=1
            m=int(math.sqrt(x))
            i=2
            while i<=m:
                if x%i==0:
                    break
                elif i==m and x%m!=0:
                    p=x
                    primo=True
                    break
                else:
                    i+=1
                    continue
    return(p)

print('\nEl número primo que se encuetra despúes de {} es el '.format(n), siguiente_primo(n))

ejecute=True
while ejecute==True:
    respuesta=input('¿Deseas vover a conocer el número primo que viene de otro número dado? ')
    if respuesta=='si':
        n=int(input('¿Con qué número queires seguir?'))
        print('El número primo que se encuetra despúes de {} es el '.format(n), siguiente_primo(n))
    elif respuesta=='no':
        print('Comprendo, te dejo continuar...')
        break
    else:
        print('recuerde que su respuesta debe ser si o no')
        continue


print('\n  15. Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6\n')

print('Si un número es multiplo de 6, quiere decir que dicho número es divisible por 6. Si un número es divisible por 6, tambien es divisible por 3. Por lo que se concluye que basta con encontrar un el primer número que sea divisible por 6:\n')

n=100
while n>=100 and n<=300:
    if n%6==0:
        break
    else:
        n+=1
        continue


