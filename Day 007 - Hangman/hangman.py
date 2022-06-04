from random import choice

def desenha(erro):
    if erro == 1:
        print(' O')
    if erro == 2:
        print(''' O\n |''')
    if erro == 3:
        print('  O\n \|')
    if erro == 4:
        print('  O\n \|/')
    if erro == 5:
        print('  O\n \|/\n  |')
    if erro == 6:
        print('  O\n \|/\n  |\n /')
    if erro == 7:
        print('  O\n \|/\n  |\n / \ ')

palavras = ['livro', 'banana', 'abacate', 'chave', 'cachorro']

palavra = choice(palavras)
jogadas = 6 #no setimo já ta enforcado
print(palavra)
oculto = []
for i in range(0, jogadas):
    oculto.append('-')

print(oculto)
erro = 0
while True:
    letra = input('Digite uma letra: ')
    for j in range(0, len(palavra)):
        if palavra[j] == letra:
            oculto[j] = letra
    print(''.join(oculto))
    if letra not in palavra:
        erro += 1
        desenha(erro)
    jogadas -= 1

    if jogadas == 0:
        print('PERDEU')
        break
    if ''.join(oculto) == palavra:
        print('GANHOU')
        break

    

