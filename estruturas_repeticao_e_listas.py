# 01. Faça um programa que leia 5 números e informe o maior número.

numeros = [1, 2, 3, 4, 5]
print(max(numeros))

'''
02. Crie uma lista de locais que você gostaria de conhecer no mundo, na ordem do local que você dá mais prioridade para o local que você dá menos prioridade. Exiba a lista nas seguintes configurações:
a) ordem original
b) ordem alfabética
c) ordem de prioridades inversa
d) quantidade de itens
'''

locais = ['Portugal', 'França', 'Inglaterra', 'Itália', 'Grécia']
print(locais)

locais.sort()
print(locais)

locais.sort(reverse=True)
print(locais)

len(locais)

'''
03. Crie uma lista com os preços dos jogos que você mais gosta.
a) Imprima o preço mais caro;
b) Imprima o preço mais barato.
'''

jogos = [32,299,199,82,42]
print(max(jogos))
print(min(jogos))

'''
'''

# 05. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

numeros = [1,2,3,4,5,6,7,8,9]
numeros = list(range(1, 50, 2))
print(numeros)

# 06. Faça um programa que recebe um número de 1 a 10 do usuário e imprime a tabuada de multiplicação desse número.

num = int(input('Digite um número de 1 a 10: '))
if num <= 0 or num >= 11:
    print('Digite um número correto')
else:
    for multi in range(1, 11):
        print(f'{num} x {multi} =', num*multi)
        
        
