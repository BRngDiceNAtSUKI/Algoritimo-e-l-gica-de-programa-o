from math import sqrt as raiz
a = float(input('valor de a:  '))
b = float(input('valor de b: '))
c = float(input('valor de c:  '))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b - raiz(delta)) / (2*a)
    x2 = (-b + raiz(delta)) / (2*a)
    print( f' x1 = {x1:.2f} | x2 = {x2:.2f}')
else:
        print('não existem raizes reais.')
