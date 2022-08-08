students = {'student':['Angela', 'James', 'Lilly'], 'score':[56, 76, 98]}

import pandas
studentsDataFrame = pandas.DataFrame(students)

print(studentsDataFrame)

for (key, value) in studentsDataFrame.items():
    print(key) #mostra os nomes das colunas
    print(value) #mostra os valores de cada coluna

for (index, row) in studentsDataFrame.iterrows():
    print(row)
    print()