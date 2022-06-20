# Create a guessing game with two levels of dificulty, the easy one with 10 attempts and the hard one with 5

from random import randint

number = randint(1, 100)

mode = (input('Escolha a dificuldade, Fácil ou Difícil: ')).upper()[0]

if mode == 'F':
    chances = 10
else: chances = 5

while chances > 0:
    num = int(input('Tente adivinhar: '))
    chances -= 1
    if chances == 0:
        print('Acabaram as Chances')
        break
    elif num > number:
        print(f'Muito alto. Tente novamente. Você tem {chances} chances')
    elif num < number:
        print(f'Muito baixo. Tente novamente. Você tem {chances} chances')
    else:
        print(f'Acertou! A resposta é {number}')
        break

