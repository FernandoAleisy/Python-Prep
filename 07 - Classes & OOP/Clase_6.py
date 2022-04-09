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