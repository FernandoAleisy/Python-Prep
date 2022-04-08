# Limpiar el terminal
import os
os.system('cls')

print('\n  1. Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla\n')

variable_1=3
print(variable_1)

print('\n  2. Imprimir el tipo de dato de la constante 8.5\n')

print(str(type(8.5))[8:-2])

print('\n  3. Imprimir el tipo de dato de la variable creada en el punto 1\n')

print(str(type(variable_1))[8:-2])


print('\n  4. Crear una variable que contenga tu nombre\n')

mi_nombre_es='Fernando Aleisy González'

print('\n  5. Crear una variable que contenga un número complejo\n')

variable_2=4-5j

print('\n  6. Mostrar el tipo de dato de la variable crada en el punto 5\n')

print(str(type(variable_2))[8:-2])

print('\n  7. Crear una variable que contenga el valor del número Pi redondeado a 4 decimales\n')

import math
variable_3=(round(math.pi,4))

print('\n  8. Crear una variable que contenga el valor "True" y otra que contenga el valor True. ¿Se trata de lo mismo?\n')

variable_4='True'
variable_5=True
if (type(variable_4)==type(variable_5)):
    print('Se trata de lo mismo, ya que son el mismo tipo de variable')
else:
    print('No se trata de lo mismo, ya que son diferentes tipos de variable, la primera es del tipo ', str(type(variable_4))[8:-2], ' y la segunda varible es del tipo ', str(type(variable_5))[8:-2],'\n')


print('\n  9. Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9\n')

print('No se crearon variables en el punto 9, aunque le puedo mostrar el tipo de variables que se crearon en el punto 8:\n')
print(str(type(variable_4))[8:-2])
print(str(type(variable_5))[8:-2])


print('\n  10. Asignar a una variable, la suma de un número entero y otro decimal\n')

variable_6=9+10.54

print('\n  11. Realizar una operación de suma de números complejos\n')

complejo_1=3+6j
print(complejo_1)
complejo_2=-2+7j
print(complejo_2)
complejo_3=complejo_1+complejo_2
print(complejo_3)

print('\n  12. Realizar una operación de suma de un número real y otro complejo\n')

real_1=3.8
print(real_1)
complejo_4=real_1+complejo_2
print(complejo_4)

print('\n  13. Realizar una operación de multiplicación\n')

numero_1=5
print(numero_1)
numero_2=7.75
print(numero_2)
resul_multiplicar=numero_1*numero_2
print(resul_multiplicar)

print('\n  14. Mostrar el resultado de elevar 2 a la octava potencia\n')

print('la octava potencia de 2 es ',2**8)

print('\n  15. Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla\n')

numero_3=39
numero_4=5
cociente_1=numero_3/numero_4
print(cociente_1)

print('\n  16. De la división anterior solamente mostrar la parte entera\n')

print(numero_3//numero_4)

print('\n  17. De la división de 27 entre 4 mostrar solamente el resto\n')

print(27%4)

print('\n  18. Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado\n')

print((7%4)**3)

print('\n  19. Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas\n')

variable_7='mi nombre es: '
print(variable_7+mi_nombre_es,'\n')

print('\n  20. Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?\n')

variable_8='2'
variable_9=2
if (variable_8==variable_9):
    print('Si son iguales, ya que ambas son del tipo', str(type(variable_8)))
else:
    print('No son iguales, ya que son diferentes tipos de variable, la primera es del tipo ', str(type(variable_8))[8:-2], ' y la segunda varible es del tipo ', str(type(variable_9))[8:-2],'\n')


print('\n  21. Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera\n')

variable_10=int(variable_8)

if (variable_10==variable_9):
    print('Si son iguales, ya que ambas son del tipo', str(type(variable_10))[8:-2], '\n')
else:
    print('No son iguales, ya que son diferentes tipos de variable, la primera es del tipo ', str(type(variable_10))[8:-2], ' y la segunda varible es del tipo ', str(type(variable_9))[8:-2],'\n')

print('\n  22. ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float("3,8")\n')

print('a=float(3,8) arroja error porque python utiliza el "." como seprador decimal en vez de la ",", por ello no puede convertir 3,8 en un número\n')

a='3,8'
a=a.replace(',','.')
a=float(a)
print(a)

print('\n  23. Crear una variable con el valor 3, y utilizar el operador "-=" para modificar su contenido\n')

variable_11=3
variable_11-=2

print('\n  24. Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?\n')

print('1<<2 da ', 1<<2, ' porque << es un operador de números binarios que el segundo número indica cuantos 0 deben agregarse a la derecha del primer número expresado en el sistema binario. En este caso, el 1 en binario es ', bin(1), ', que agregandole 2 ceros a la derecha se optine ', bin(1<<2), ', el cual, en el sistema decimal es ', int(0b100),'\n')

print('El sistem de numeración binaria es el sitema en el que se utilizan solo dos digitos (0 y 1) para representar las cantidades. Es el sistema numeración utilizado por los computadores y en general, por los sistemas digitales\n')

print('\n  25. Realizar la operación 2 + "2" ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?\n')

print('La operación no esta permitida porque el primer mienbro de la adición es un número y el segundo es un una cadena de texto o string y solo se puede calcular la suma de números y la concatenación de cadenas de texto\n')
print('Al ser del mismo tipo los dos operadores, el resultado de la operación depende del tipo de variable al que corresponde los operadores. Si los operdores son del tipo string, el resultado sería "22", si son del tipo int, el resultado sería 4\n')

print('\n  26. Realizar una operación válida entre valores de tipo entero y string\n')

print(7+int('4'))


