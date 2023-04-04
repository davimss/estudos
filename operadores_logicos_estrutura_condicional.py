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

# 05. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Digite o dia: '))
if dia <= 0:
    print('Dia inválido')
elif dia > 31:
    print('Dia inválido')
else:
    mes = int(input('Digite o mês: '))
    if mes <= 0:
        print('Mês inválido')
    elif mes > 12:
        print('Mês inválido')
    else:
        ano = int(input('Digite o ano: '))
        if ano <= 0000:
            print('Ano inválido')
        elif ano > 2023:
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
