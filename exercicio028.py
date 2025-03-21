import random
from time import sleep
n1 = random.randint(0, 5)
print('O computador está pensando em um número entre 0 e 5...')
sleep(3)
print('\033[1;33mPensou!\033[m')
adv = int(input('Tente adivinhar o número que o computador pensou: '))
if n1 == adv:
    print('\033[32mParabéns, você acertou o número que o computador estava pensando!\033[m')
else:
    print('\033[31mÉ... você errou o número que o computador estava pensando :(')
