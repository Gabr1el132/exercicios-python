num = int(input('Digite a distância da sua viagem em km: '))
if num <=200:
    passagem = num * 0.50
    print('A passagem custará R${}'.format(passagem))
else:
    passagem = num * 0.45
    print('A passagem custará R${}'.format(passagem))
