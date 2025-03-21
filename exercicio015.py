dia = int(input('Por quantos dias o carro esteve alugado? '))
km = float(input('Quantos quilômetros o carro rodou? '))
print('Você terá que pagar R${} por {} dias alugados e {} quilômetros rodados.'.format(dia * 60 + km * 0.15, dia, km))