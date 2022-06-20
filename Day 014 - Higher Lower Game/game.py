
from data import data
from random import choice

pontos = 0

c1 = choice(data)

while True:

    c2 = choice(data)
    #colocar condiçao p/ não serem iguais
    s1 = c1['follower_count']
    s2 = c2['follower_count']

    print(f"Compare A: {c1['name']}, um(a) {c1['description']}, dos {c1['country']}\n")
    print('VS\n')
    print(f"Contra B: {c2['name']}, um(a) {c2['description']}, dos {c2['country']}\n")
    
    escolha = input('Quem tem mais seguidores? A ou B? ').upper()
    
    if escolha == 'A' and s1 > s2:
        pontos += 1
    elif escolha == 'B' and s2 > s1:
        pontos += 1
        c1 = c2
    else:
        print(f'Errado! Pontuação final: {pontos}')
        break