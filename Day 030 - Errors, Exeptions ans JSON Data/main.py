

try:
    file = open('Day 030 - Errors, Exeptions ans JSON Data/teste.txt') #tentando abrir um arquivo que não existe
    dicionario = {'key':'value'}
    print(dicionario['aaaa']) #tentando mostrar uma key que não existe
except FileNotFoundError: 
    file = open('Day 030 - Errors, Exeptions ans JSON Data/teste.txt', 'w')
    file.write('Something')
except KeyError as error_message:
    print(f'A chave {error_message} não existe')
else:
    conteudo = file.read()
    print(conteudo)
finally:
    file.close()
    print('Arquivo fechado')

#-----------------------------------------#

altura = float(input('Altura: '))
peso = float(input('Peso: '))

if altura > 3:
    raise ValueError('Altura não pode ser maior do que 3 metros')

imc = peso/altura ** 2
print(imc)