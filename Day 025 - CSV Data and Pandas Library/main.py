#Modo ineficiente -> 'bruto' de trabalhar com os arquivos
#with open('Day 025 - CSV Data and Pandas Library\weather_data.csv', 'r') as Wdata:
#    dados = Wdata.readlines()
#    print(dados)


#Usando a biblioteca CSV embutida no Python, que também é trabalhosa
#import csv 
#with open('Day 025 - CSV Data and Pandas Library\weather_data.csv', 'r') as Wdata:
#    dados = csv.reader(Wdata)
#    temperaturas = []
#    for linha in dados:
#        print(linha)
#        if linha[1] != 'temp':
#            temperaturas.append(int(linha[1]))
#    print(temperaturas)

import pandas

#Mostra somente a coluna das temperaturas
dados = pandas.read_csv('Day 025 - CSV Data and Pandas Library\weather_data.csv')
print(dados['temp'])

#Converte todo o conjunto de dados em dicionários
dadosDict = dados.to_dict()
print(dadosDict)

#Converte somente as temperaturas pra uma lista
dadosTempList = dados['temp'].to_list()
print(dadosTempList)

#Calcula a média sem usar pandas
print(sum(dadosTempList) / len(dadosTempList))

#Calcula a média usando Pandas
print(dados['temp'].mean())

#Maior valor
print(f'A maior temperatura é {dados["temp"].max()}\n')
print(f'A maior temperatura é {dados.temp.max()}\n')

#Dados das Linhas
print(dados[dados.day == 'Monday']) #Procurando na coluna DAY, me dê a linha que começa com 'Monday'
                                    #Note que está tudo dentro de [], ou seja, é o índice

#Qual linha possui a maior temperatura
print(dados[dados.temp == dados.temp.max()])
#Na coluna de temperatura (TEMP), ele procura a LINHA que seja igual a temperatura máxima

monday = dados[dados.day == 'Monday'] #pega a linha MONDAY
print(monday.condition) #da linha monday, pega a coluna condition

#Criando um DataFrame do ZERO

dados_dict = { #Criação de um dicionário normal
    'student;s':['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

d = pandas.DataFrame(dados_dict)
print(d)