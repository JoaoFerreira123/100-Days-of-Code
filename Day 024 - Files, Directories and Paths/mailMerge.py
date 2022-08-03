with open('Day 024 - Files, Directories and Paths/names.txt', 'r') as names:
    nomes = names.readlines()

with open('Day 024 - Files, Directories and Paths\startingLetter.txt', 'r') as letter:
    finalLetter = letter.read()
    for nome in nomes:
        n = nome.strip()
        newLetter = finalLetter.replace('[nome]', n)
        with open(f'Day 024 - Files, Directories and Paths\doneLetters/carta_{n}.txt', 'w') as doneLetter:
            doneLetter.write(newLetter)

