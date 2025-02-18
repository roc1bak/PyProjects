import random
a = input('Digite um nome: ')
b= input('Digite um nome: ')
c= input ('Digite um nome: ' )
d= input('Digite um nome: ')
lista = [a,b,c,d]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))