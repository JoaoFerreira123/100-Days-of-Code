# Construir o jogo 21 -> Dois jogadores jogam cartas e tentam chegar ao maior número possível, 
# sem ultrapassar 21. Se ultrapassar o jogador perde.
# Com cartas de 2 a 10, cada valor é o literal de cada carta, exceto J, Q e K que contam como 10
# Tem tbm o A, que vale 1 ou 11, cabendo ao jogador decidir se quer adicionar 1 ou 11
# Há a possibilidade de empate

# O jogador só vê a primeira carta do oponente, sem saber a outra e escolhe se quer pegar mais uma carta
# Ou se quer virar as cartas e obter o resultado. Se o jogador escolher pegar mais uma carta, o oponente
# também pega mais uma. Se escolher virar as cartas, vence o que tiver o maior número <= 21

from random import choice

cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def escolhe():
    cc.append(choice(cartas))
    cp.append(choice(cartas))

def over():
    print(f'Suas cartas finais: {cp}, pontuação final: {sum(cp)}')
    print(f'Cartas finais do Computador: {cc}, pontuação final: {sum(cc)}')
    

cc = []
cp = []

cont = 'S'
while cont != 'N':
    escolhe() #jogador e pc começam com 2 cartas
    escolhe()
    while True:
        print(f'Suas Cartas: {cp}, pontuação atual: {sum(cp)} ')
        print(f'Primeira Carta do Computador: {cc[0]}')
        op = input('Digite N para pegar uma nova carta e P para passar: \n').upper()
        if op == 'N':
            escolhe()
            if sum(cp) > 21 or sum(cc)>21:
                over()
                break
        if op == 'P':
            over()
            break

    if sum(cp) > 21 or sum(cc) == 21 or sum(cc) > sum(cp):
        print('Você Perdeu')
    elif sum(cp) == sum(cc):
        print('Empate')
    else:
        print('Você Ganhou!!')

    cont = input('\nQuer jogar novamente? [S] ou [N] \n').upper()[0]
    if cont == 'S':
        cp.clear()
        cc.clear()
    