n1 = input('Digite uma cadeia de caracteres: ').upper()
print('A letra A aparece {} vez(es).'.format(n1.count('A')))
print('Essa letra aparece pela primeira vez na {}ª posição.'.format(n1.find('A') + 1))
print('Essa letra aparece pela última vez na {}ª posição.'.format(n1.rfind('A') + 1))