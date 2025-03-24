a = float(input('a?  '))
b = float(input('b?  '))
c = float(input('c?  '))
print('triangulo', end='  ')

if a == b and b == c:
    print('equilatero')
else:
    if a == b or b == c or a == c:
          print('isósceles')
    else:
          print('escaleno')
