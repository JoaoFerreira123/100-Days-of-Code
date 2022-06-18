from replit import clear

lances = {}

while True:
    nome = input('Nome do Comprador: ')
    lances[nome] = float(input('Qual o valor do Lance R$: '))
    
    op = input('Há mais compradores? [S] ou [N]? ').upper()[0]
    clear()
    if op == 'N':
        break

maior = 0
for i in lances:
    if lances[i] > maior:
        maior = lances[i]
        nome = i

print(f'O vencedor é {nome} com um lance de R$:{maior}')