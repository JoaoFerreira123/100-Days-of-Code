#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

dados = pandas.read_csv('Day 026 - Day Comprehension/nato_phonetic_alphabet.csv')
alf_fonetico = {linha.letra:linha.codigo for (codigo, linha) in dados.iterrows()}

palavra = input('Digite uma palavra: ').upper().strip()
codigos = [alf_fonetico[letra] for letra in palavra]
print(codigos)