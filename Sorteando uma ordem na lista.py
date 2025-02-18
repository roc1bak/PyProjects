from random import shuffle
a = input('Digite um nome: ')
b= input('Digite um nome: ')
c= input ('Digite um nome: ' )
d= input('Digite um nome: ')
lista = [a,b,c,d]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)