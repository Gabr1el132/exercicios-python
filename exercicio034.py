salario = float(input('Digite o valor do salário: '))
if salario > 1250.00:
    aumento = salario * 0.1
    print('O aumento será de R${:.2f}.'.format(aumento))
else:
    aumento = salario * 0.15
    print('O aumento será de R${}.'.format(aumento))
    