from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador pensar
print('-=-'*20)
print('Vou pensar em um número de 0 a 5, Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador ==computador:
    print("PARABÉNS!!! VOCÊ CONSEGUIU!!!")
else:
    print("Você errou o número escolhido foi ", computador)




