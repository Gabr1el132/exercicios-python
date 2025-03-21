ano = int(input('Digite um ano: '))
if ano % 4 == 0 or ano % 400 == 0:
    print('\033[1;32mEste ano é bissexto.')
else:
    print('\033[1;31mEste ano não é bissexto.')
