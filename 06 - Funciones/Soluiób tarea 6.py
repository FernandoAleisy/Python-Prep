print('Funciones')

print('\n1. Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es\n')

def es_primo(x):
    valor=True
    y=int(x**0.5)
    i=2
    while i<=y:
        if x%i==0:
            valor=False
            break
        else:
            i+=1
    return(valor)

es_primo(15)

print('\n2. Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista\n')

def primos(y):
    if type(y)!=list:
        print('error, esta función requiere como argumento una lista')
    else:
        lista=[]
        for x in y:
            if es_primo(x):
                lista.append(x)
            else:
                continue
    return(lista)

numeros=[3,7,9,15,23,31,32]
primos(numeros)

print('\n3. Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera\n')

def repetido(x):
    if type(x)!=list:
        print('error, esta función requiere como argumento una lista')
        numero='N/A'
        veces='N/A'
    else:
        numero=''
        veces=0
        if len(x)==0:
            numero='N/A'
            veces='N/A'
        else:
            for i in x:
                if x.count(i)<veces:
                    continue
                elif x.count(i)==veces:
                    import random
                    numero=random.choice([i,numero])
                else:
                    numero=i
                    veces=x.count(i)
    return(numero,veces)

numeros=[3,3,9,15,9,31,9,25,3]
numero,veces=repetido(numeros)
print('El número que más se repite es {} y lo hace {} veces'.format(numero,veces))

print('\n4. A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.\n')

def mas_repetidos(x,y):
    numero,veces=repetido(x)
    if y==False:
        for i in range(1,veces+1):
            x.remove(numero)
    numero,veces=repetido(x)
    return(numero,veces)

numeros=[3,3,9,15,9,31,9,25,3]
numero,veces=mas_repetidos(numeros,True)
print('El número que más se repite es {} y lo hace {} veces'.format(numero,veces))
numero,veces=mas_repetidos(numeros,False)
print('El segundo número que más se repite es {} y lo hace {} veces'.format(numero,veces))

print('\n5. Crear una función que convierta entre grados Celsius, Farenheit y Kelvin\n')
print('\nFórmula 1	: (°C × 9/5)+ 32 = °F<br>\n')
print('\nFórmula 2	: °C + 273.15 = °K<br>\n')
print('\nDebe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino\n')

def Conver_temp(x,y,z):
    """El primer argumento debe ser un número, el segundo la unidad de origen ('c', 'f', 'k') y el terer elemento es la unidad de destino ('c', 'f', 'k')"""
    if y in ['c','f','k']:
        if z in ['c','f','k']:
            if y==z:
                return(x)
            else:
                if y=='c':
                    if z=='f':
                        x=x*9/5+32
                    else:
                        x=x+273.15
                elif y=='f':
                    if z=='c':
                        x=(x-32)*5/9
                    else:
                        x=(x-32)*5/9+273.15
                else:
                    if z=='c':
                        x=x-273.15
                    else:
                        x=(x-273.15)*9/5+32
                return(x)
        return('falta la medida de destino')
    return('falta la medida de origen y la medida de destino')

c=0
print(c,'°C=',Conver_temp(c,'c','f'),'°F')
print(c,'°C=',Conver_temp(c,'c','k'),'K')

print('\n6. Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:\n')

Temperauras_c=[0,24,100]
Temp=iter(Temperauras_c)
for i in Temp:
    for j in ['c','f','k']:
        print(i,'°C=',Conver_temp(i,j,'c'),'°',j)

print('\n7. Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo\n')

def factorial(x):
    '''Debes ingresar un número entero no negativo'''
    y=1
    if x<0 or type(x)==float:
        return('N/A')
    elif x in [0,1]:
        return(1)
    else:
        for i in range(1,x+1):
            y=y*i
        return(y)

factorial(5)