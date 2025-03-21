r1 = int(input('Digite um valor: '))
r2 = int(input('Digite outro valor: '))
r3 = int(input('Digite mais um valor: '))
if r2 - r3 < r1 < r2 + r3 and r1 - r3 < r2 < r1 + r3 and r1 - r2 < r3 < r1 + r2:
    print('Essas 3 retas podem criar um triângulo.')
else:
    print('Essas 3 retas não podem criar um triângulo.')
