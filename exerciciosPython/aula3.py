'''
EXERCICIO:
Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela esta apta a ser do Exercito
Para entrar no exercito é preciso ter mais de 18 anos
pesar mais ou igual  60 kilos
e medir mais ou igual 1,70 metros
'''

idade = int(input('Escreva sua idade: '))
peso = float(input('Escreva seu peso: '))
altura = float(input('Escreva sua altura: '))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('\nVoce esta apto a servir o exercito\n')
else:
    print('\nVoce nao esta apto\n')
