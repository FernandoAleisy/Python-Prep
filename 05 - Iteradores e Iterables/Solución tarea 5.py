import os
os.system('cls')

print('\n 1. A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1\n')

numeros=list()
i=15
while i>=1:
    numeros.append(-i)
    i-=1
print(numeros)

print('\n2. ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?\n')

i=1
texto=''
while i<15:
    texto=texto+', '+str(numeros[i])
    i+=2
print(texto[1:])

print('\n3. Resolver el punto anterior sin utilizar un ciclo while\n')

texto=''
for i in range(1,15,2):
    texto=texto+', '+str(numeros[i])
print('\nLos números pares de la lista son: ',texto[1:])

print('\n4. Utilizar el iterable para recorrer sólo los primeros 3 elementos\n')

texto=''
for i in range(0,3):
    texto=texto+', '+str(numeros[i])
print('\nLos primeros 3 elementos de la lista son: ',texto[1:])

print('\n5. Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento\n')

print('\n6. Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]\n')

lista = [1,2,5,7,8,10,13,14,15,17,20]
for i in range(1,21):
    if i in lista:
        continue
    else:
        lista.insert(i-1,i)
        pass
print(lista)

print('\n7. La sucesión de Fibonacci es un listado de números que sigue la fórmula:\n')
print('\n<br>\n')
print('\nn<sub>0</sub> = 0<br>\n')
print('\nn<sub>1</sub> = 1<br>\n')
print('\nn<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>\n')
print('\nCrear una lista con los primeros treinta números de la sucesión\n')

fibonacci=[0,1]
for i in range(2, 30):
    fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
    continue

print(fibonacci)

print('\n8. Realizar la suma de todos elementos de la lista del punto anterior\n')

print(sum(fibonacci))

print('\n9. La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:\n')

print('Donde i es la cantidad total de elementos\n')
print('n\u1d62/n\u1d62\u208b\u2081')
print('n\u1d62\u208b\u2081/n\u1d62\u208b\u2082')
print('n\u1d62\u208b\u2082/n\u1d62\u208b\u2083')
print('n\u1d62\u208b\u2083/n\u1d62\u208b\u2084')
print('n\u1d62\u208b\u2084/n\u1d62\u208b\u2085\n')

n=len(fibonacci)-1
for i in range(n, n-5,-1):
    print(fibonacci[i]/fibonacci[i-1])

print('\n10. A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"\n')

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

n=[]
for i, j in enumerate(cadena):
    if j=='n':
        n.append(i)
    else:
        pass
print('La letra n aparece en las posiciones: ', str(n)[1:-1])

print('\n11. Crear un diccionario e imprimir sus claves utilizando un iterador\n')

ciudades = {  'Ciudad': ['Bogotá','Villavicencio','Cali'], 
'Departamento': ['Cundinámarca','Meta','Valle del cauca'], 
'Población' : [7878783,531275,2227642]}
for i in ciudades:
    print(i)

print('\n12. Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador\n')

ciudades_lista=cadena.split(' ')
ciudades_lista
palabras=iter(ciudades_lista)
for i in range(0,len(ciudades_lista)):
    print(next(palabras))

print('\n13. Crear dos listas y unirlas en una tupla utilizando la función zip\n')

lista_1=['cama','nevera','moto','carro','televisor']
lista_2=[4,2,2,1,2]
dupla_1=(zip(lista_1,lista_2))
print('La variable dupla_1 es del tipo: ',str(type(dupla_1))[8:-2])
print(list(dupla_1))

print('\n14. A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7\n')

lis=[18,21,29,32,35,42,56,60,63,71,84,90,91,100]
divisibles_7=[]
for i in lis:
    if i%7==0:
        divisibles_7.append(i)
print(divisibles_7)

print('\n15. A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:\n')

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
print(len(lis))

print('\n16. Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es\n')

for i in lis:
    if type(i)!=list:
        indice=lis.index(i)
        lis[indice]=i.split(' ')
print(lis, '\n')
