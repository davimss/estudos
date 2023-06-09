# 01. Informe a saída das seguintes expressões:

# a)
3 < 8 # True

# b)
a = 12
b = a - 10
a > b # False

# c)
16 != 16 # False

# d)
2 < 5 > 10 # False

# e)
3 <= 5 >= 2 # False

# 02. Verifique se as igualdades abaixo são verdadeiras:

# a)
2 * 2.0 == 4 # True

# b)
2 * 3 == 5 # False

'''
c)  4a+3=b , para  a=3  e  b=15 
P.S.: primeiro declare as variáveis a e b
'''
a = 3 
b = 15
4*3 + 3 == b # True

'''
03. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores, sendo encerrado;

b) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

import math
a = int(input('Digite o valor de a: '))
if a != 0:
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))

    d = b**2 - 4*a*c
    if d < 0:
        print('O valor de delta é negativo. A equação não possui raizes reais')
    else:
        x1 = (-b + d**(1/2)) / (2*a)
        print(f"x' = {x1}")
        if d == 1:
            x2 = (-b - d**(1/2)) / (2*a)
            print(f"x'' = {x1}")
            
# 04. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('Digite o ano: '))
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')

# 05. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Digite o dia: '))
if dia <= 0 or dia > 31:
    print('Dia inválido')
else:
    mes = int(input('Digite o mês: '))
    if mes <= 0 or mes > 12:
        print('Mês inválido')
    else:
        ano = int(input('Digite o ano: '))
        if ano <= 0 or ano > 2099:
            print('Ano inválido')
        else:
            print(f'{dia}/{mes}/{ano} é uma data válida')
            
# 06. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print('1-Domingo, 2-Segunda, 3-Terça\n4-Quarta, 5-Quinta, 6-Sexta, 7-Sábado')
num = int(input('Digite um número de 1 a 7: '))
if num == 1:
    print('Domingo')
elif num == 2:
    print('Segunda')
elif num == 3:
    print('Terça')
elif num == 4:
    print('Quarta')
elif num == 5:
    print('Quinta')
elif num == 6:
    print('Sexta')
elif num == 7:
    print('Sábado')
else:
    print('Dia inválido')
    
# 08. Faça um código para imprimir uma mensagem informando se um aluno foi aprovado ou reprovado em uma disciplina com base em sua nota final.
# A nota mínima necessária para aprovação é 5.

nota = int(input('Digite a nota do aluno: '))
if nota >= 5 and nota <= 10:
    print('Aluno Aprovado')
elif nota > 10:
    print('Digite uma nota válida')
else:
    print('Aluno Reprovado')
