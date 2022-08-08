#Eleve ao quadrado os números da lista usando List Comprehension
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
quadrado = [n**2 for n in numbers]
print(quadrado)

#Filtre os números pares
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
pares = [i for i in numbers if i%2 == 0]
print(pares)

#Cria uma lista que possui os elementos comuns a duas listas
lista1 = [3,6,5,8,33,12,7,4,72,2,42,13]
lista2 = [3,6,13,5,7,89,12,3,33,34,1,344,42]
comum = [int(num) for num in lista1 if num in lista2]
print(comum)

#Cria um dicionário a partir de uma frase, onde a key é cada palavra e o value é a quantidade de letras
frase = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {palavra:len(palavra) for palavra in frase.split(' ')}
print(result)