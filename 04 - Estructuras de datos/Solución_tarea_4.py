from operator import index
import os
os.system('\ncls\n')

## Estructuras de Datos

print('\n1. Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla\n')

ciudades=['Villavicencio', 'Bogotá', 'Cali', 'Bucaramanga', 'Medellin', 'Neiva', 'Pasto']
print(ciudades)

print('\n2. Imprimir por pantalla el segundo elemento de la lista\n')

print(ciudades[1])

print('\n3. Imprimir por pantalla del segundo al cuarto elemento\n')

print(ciudades[1:4])

print('\n4. Visualizar el tipo de dato de la lista\n')

print('El tipo de la variable ciudades es: ', str(type(ciudades))[8:-2])

print('\n5. Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento\n')

print(ciudades[2:])

print('\n6. Visualizar los primeros 4 elementos de la lista\n')

print(ciudades[:4])

print('\n7. Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?\n')

print('Arroja error si trato de insertar las dos ciudades a la vez con el comando .append. Aunque se puede agregar primero una ciudad y luego la otra al usar este comando. Támbien se pueden agragar las ciudades a la vez con el comando .extend')

#ciudades.append('Villavicencio', 'Cartagena')

ciudades.append('Villavicencio')
ciudades.append('Cartagena')

#ciudades.extend(['Villavicencio', 'Cartagena'])
print(ciudades)

print('\n8. Agregar otra ciudad, pero en la cuarta posición\n')

ciudades.insert(3,'Yopal')
print(ciudades)

print('\n9. Concatenar otra lista a la ya creada\n')

ciudades.extend(['Leticia', 'Acacias'])
print(ciudades)

print('\n10. Encontrar el índice de la ciudad que esta en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?\n')

indice=ciudades.index('Villavicencio')
print(indice)
print('\n .index devuelve solo la primera posición de la ciudad duplicada')

print('\n11. ¿Qué pasa si se busca un elemento que no existe?\n')

#indice=ciudades.index('Carro')
#print(indice)
print('\n Python devuelve error')

print('\n12. Eliminar un elemento de la lista\n')

ciudades.remove('Villavicencio')
print(ciudades)

print('\n13. ¿Qué pasa si el elemento a eliminar no existe?\n')

#ciudades.remove('Carro')
print('\n Python devuelve error')

print('\n14. Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo\n')

ciudad=ciudades.pop()
print(ciudad)
print('\nSe denota que la ciudad {} ya no está en la lista ciudades: '.format(ciudad), ciudades)

print('\n15. Mostrar la lista multiplicada por 4\n')

print(ciudades*4)

print('\n16. Crear una tupla que contenga los números enteros del 1 al 20\n')

numeros_enteros=tuple(range(1,21))
print('La variable numeros_enteros es del tipo: ', str(type(numeros_enteros))[8:-2])
print(numeros_enteros)

print('\n17. Imprimir desde el índice 10 al 15 de la tupla\n')

print(numeros_enteros[10:16])

print('\n18. Evaluar si los números 20 y 30 están dentro de la tupla\n')

def eval_existencia(x,y):
    if x in y:
        print('{} esta en la tupla'.format(x))
    else:
        print('{} no esta en la tupla'.format(x))

eval_existencia(15,numeros_enteros)
eval_existencia(30,numeros_enteros)


print('\n19. Con la lista creada en el punto 1, validar la existencia del elemento "París" y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.\n')

ciudad='París'
if ciudad in ciudades:
    print('La ciudad {} existe en la lista ciudades',format(ciudad))
else:
    ciudades.append(ciudad)
    print('La ciudad {} no existe en la lista ciudades, pero se agrego al final de la lista: ',format(ciudad))

print(ciudades)

print('\n20. Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista\n')

a='Bogotá'
if ciudades.count(a)==1:
    print('La ciudad {} esta '.format(a), ciudades.count(a), ' vez')
elif ciudades.count(a)==1:
    print('La ciudad {} esta '.format(a), ciudades.count(a), ' veces')
else:
    print('La ciudad {} no esta'.format(a))

b=15
if numeros_enteros.count(b)==1:
    print('El número {} esta '.format(b), numeros_enteros.count(b), ' vez')
elif numeros_enteros.count(b)==1:
    print('El número {} esta '.format(b), numeros_enteros.count(b), ' veces')
else:
    print('El número {} no esta'.format(b))


print('\n21. Convertir la tupla en una lista\n')

lista_enteros=list(numeros_enteros)
print('la variable lista_enteros es del tipo: ',str(type(lista_enteros))[8:-2])

print('\n22. Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables\n')

#Metodo extenso
#n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20=numeros_enteros
#print('n1=',n1,', n2=',n2,', n3=',n3)

#Metodo comprimido:

numeros_2=tuple(numeros_enteros[:3])
n1, n2, n3=numeros_2
print('n1=',n1,', n2=',n2,', n3=',n3)


print('\n23. Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".\n')

ciudades.remove('París')
mi_diccionario={'ciudades':ciudades, 'País':'Colombia', 'Continente':'América del Sur'}

print('\n24. Imprimir las claves del diccionario\n')

print(mi_diccionario.keys())

print('\n25. Imprimir las ciudades a través de su clave\n')

print(mi_diccionario['ciudades'],'\n')