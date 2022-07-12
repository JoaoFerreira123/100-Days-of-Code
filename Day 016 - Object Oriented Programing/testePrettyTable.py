from prettytable import PrettyTable

table = PrettyTable() #criando a tabela, que é um objeto da classe PrettyTable


table.field_names = ['Pokemon Name', 'Type']
#adicionado os campos da tabela

table.add_row(['Pikachu','Electric'])
table.add_row(['Squirtle', 'Water'])
table.add_row(['Charmander', 'Fire'])
#adicionando os dados na tabela linha por linha
#Note que é em sequência, cada elemento da lista é uma coluna
#Note que são usadas listas

print(table)

#Como essa tabela tem menos colunas do que linhas, 
#faria mais sentido cria-la usando as colunas, com menos código
table2 = PrettyTable()

table2.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table2.add_column('Type', ['Electric', 'Water', 'Fire'])
#Note que o primeiro argumento é o FIELD NAME, e o segundo argumento é uma lista com os elementos das colunas

table2.align = 'l'
#alinhando a tabela na esquerda (left)
print(table2)

