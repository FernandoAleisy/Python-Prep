def factoria(x):
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

factoria(5)