velocidade = int(input('Digite a velocidade do carro em km/h: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print('Você terá de pagar uma multa de R${}.'.format(multa))
else:
    print('Não houve multas para essa velocidade.')