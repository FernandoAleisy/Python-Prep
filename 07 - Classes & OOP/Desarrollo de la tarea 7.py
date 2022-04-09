import os
os.system('cls')

print(str.upper('Clases y Programación Orientada a Objetos'))

print('\n1. Crear la clase vehículo que contenga los atributos:')
print('\nColorprint')
print('\nSi es moto, auto, camioneta ó camión')
print('\nCilindrada del motor')

class Vehiculo:
    def _init_(self, color, tipo, cilindraje):
        self.color=color
        self.tipo=tipo
        self.cilindrada=cilindraje

print('\n2. A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:')
print('\nAcelerar')
print('\nFrenar')
print('\nDoblar')

class Vehiculo:
    def _init_(self, color, tipo, cilindraje):
        self.color=color
        self.tipo=tipo
        self.cilindrada=cilindraje
        self.velocidad=0
    
    def acelerar(self, aceleración, tiempo):
        self.velocidad+=aceleración*tiempo

    def frenar(self, frenado):
        self.velocidad-=frenado

    def doblar(self, grados):
        self.direccion+=grados

print('\n3. Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado')

Vehiculo1=Vehiculo('gris','carro',2400)
Vehiculo2=Vehiculo('roja','moto',400)
Vehiculo3=Vehiculo('verde','bus',5000)

Vehiculo1.acelerar(10,5)
Vehiculo2.frenar(5)
Vehiculo3.doblar(-50)

print('\n4. Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada')

class Vehiculo:
    def __init__(self, color, tipo, cilindraje):
        self.color=color
        self.tipo=tipo
        self.cilindrada=cilindraje
        self.velocidad=0
        self.direccion=0
    
    def acelerar(self, aceleración, tiempo):
        self.velocidad+=aceleración*tiempo

    def frenar(self, frenado):
        self.velocidad-=frenado

    def doblar(self, grados):
        self.direccion+=grados
    
    def estado(self):
        print('El/la {} viaja a una velocidad de {} km/h en la dirección de {}°'.format(self.tipo,self.velocidad,self.direccion))

    def caracteristicas(self):
        print('Es es un o una {} de color {} y con una cilindrada de {} cc'.format(self.tipo,self.color,self.cilindrada))


Vehiculo1.estado()
Vehiculo2.caracteristicas()

print('\n5. Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6')
print('\nVerificar Primo')
print('\nValor modal')
print('\nConversión grados')
print('\nFactorial')

class clase_6:
    def __init__(self):
        pass

    def es_primo(self,x):
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
    
    def repetido(self,x):
        '''Recuerde que esta función requiere como argumento una lista de números'''
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

    def Conver_temp(self,x,y,z):
        '''El primer argumento debe ser un número, el segundo la unidad de origen ('c', 'f', 'k') y el terer elemento es la unidad de destino ('c', 'f', 'k')'''
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

print('\n6. Probar las funciones incorporadas en la clase del punto 5')

probar=clase_6()

print(probar.es_primo(17))
print(probar.es_primo(20))
print(probar.Conver_temp(24,'c','f'), '°f')

print('\n7. Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas')

print('Si es necesario')

print('\n8. Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones')

