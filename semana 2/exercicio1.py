'''
Exercício 1:
 Crie um programa que lê dois número
 inteiros do teclado e após imprime 
 o maior números dentre eles.
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1>n2:
    print('O maior número entre eles é: {}'.format(n1))
else:
    print('O maior número entre eles é: {}'.format(n2))