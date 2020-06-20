from random import randint
nome = 'Leandro'
sobrenome = "Lima"
lastname = "Silva"
st1 = "VASCO"
numberRandom = randint(0,5)
lista =['vasco','da','gama',8,9,17]

print(f"Is the name Leandro? {nome == 'Leandro'}")

print(f"Is vasco written in lower case? {'vasco' == st1}")

print(f"Is vasco the lower case style of VASCO? {st1.lower() == 'vasco'}")

print(f'Is the random number equal to 4? {numberRandom == 4}')

print(f'Is the random number diffrent from 7? {numberRandom == 7}')

print(f'Is the random number greater than 2? {numberRandom > 2}')

print(f'Is the random number lesser than 1? {numberRandom < 1}')

print(f'Is the random number greater or equal to 1? {numberRandom >= 1}')

print(f'Is the random number lesser or equal to 5? {numberRandom <= 5}')

print(f"{nome} and {sobrenome} begins with L? {nome[0] == 'L' and sobrenome[0] == 'L'}")

print(f"Is there a letter S in {nome} or in {lastname}? {'S' in nome or 'S' in lastname}")

print(f"Is Coisa in the list \"lista\"? {'Coisa' in lista}")

print(f'Vasco is not in the list \"lista\"! {"Vasco" not in lista}')

print(f'vasco is in the list \"lista\"! {"vasco" in lista}')