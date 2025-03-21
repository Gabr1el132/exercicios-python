import math
co = float(input('Digite o valor do cateto oposto do triângulo: '))
ca = float(input('Digite o valor do cateto adjacente do triângulo: '))
print('O valor da hipotenusa desse triângulo é igual a {:.3f}.'.format(math.hypot(co, ca)))