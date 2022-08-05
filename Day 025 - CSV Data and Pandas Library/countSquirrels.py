# Contar a quantidade de Esquilos de cada cor

import pandas as pd

dados = pd.read_csv('Day 025 - CSV Data and Pandas Library\Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

cores = dados['Primary Fur Color']

with open('Day 025 - CSV Data and Pandas Library\ContagemEsquilos.csv', 'w') as contEsq:
    contEsq.writelines(str(cores.value_counts()))

#também poderia usar o método .to_csv() do Pandas