# 01. Faça um programa que peça um número e então mostre a mensagem O número informado foi [número].

num = input('Digite um número: ')
print('O número informado foi: ', num)

# 02. Faça um programa que peça dois números e imprima a soma.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
soma = num1 + num2
print('{} + {} = {}'.format(num1, num2, soma))

# 03. Faça um programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
media = (nota1+nota2+nota3+nota4)/4
print('Média: ', media)

# 04. Faça um programa que converta metros para centímetros.

m = float(input('Metros: '))
cm = m * 100
print('Centimetros: ', cm)

# 05. Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input('Raio do círculo: '))
pi = 3.14
area = pi*raio*raio
print('A área do círculo é: ', area)

# 06. Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = int(input('Tamanho da lateral do quadrado: '))
area = lado*lado
dobro = area*2
print('Dobro: ', dobro)

# 07. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganha = float(input('Quanto você ganha por hora: '))
horas = float(input('Quantas horas você trabalha: '))
salario = ganha*horas
print('Salário: ', salario)

# 08. Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input('Temperatura em Fahrenheit: '))
celsius = (fahrenheit-32)*5/9
print('Temperatura em Celsius: ', celsius)

# 09. Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input('Temperatura em Celsius: '))
fahrenheit = (celsius*9/5)+32
print('Temperatura em Fahrenheit: ', fahrenheit)

'''
10. Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
O produto do dobro do primeiro com metade do segundo.
Soma do triplo do primeiro com o terceiro.
Terceiro elevado ao cubo.
'''

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = float(input('Digite um número real: '))
print ('Produto:', ((2*num1) * (num2/2)))
print ('Soma:', (3 * num1) + num3)
print ('Cubo:', num3**3)

'''
11. Tendo como dado de entrada a altura ( h ) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens:  (72.7×h)−58 
Para mulheres:  (62.1×h)−44.7
'''

h = float(input('Altura do homem: '))
m = float(input('Altura da mulher: '))
pesoh = (72.7*h)-58
pesom = (62.1*m)-44.7
print('Peso do homem: ', pesoh)
print('Peso da mulher: ', pesom)

'''
12. Tendo como dado de entrada a altura ( h ) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens:  (72.7×h)−58 
Para mulheres:  (62.1×h)−44.7
'''

h = float(input('Altura do homem: '))
m = float(input('Altura da mulher: '))
pesoh = (72.7*h)-58
pesom = (62.1*m)-44.7
print('Peso do homem: ', pesoh)
print('Peso da mulher: ', pesom)

# 13.Faça um programa que receba do usuario uma string. O programa imprime a string sem suas vogais.

texto = str(input('Digite uma frase: '))
semVogais = texto.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
print('Nova frase: ', semVogais)
