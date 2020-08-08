from os import system
from random import randint
import time

system("cls")

start = time.time()


favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python'}

favorite_languages['helton'] = ""
favorite_languages['jonhathan'] = "c#"
favorite_languages['wesley'] = ""
favorite_languages['leandro'] = "matlab"
favorite_languages['carlao'] = "python"
favorite_languages['rodrigo'] = ""

for key,value in favorite_languages.items():
	print(f'{key}s Favorite language: {value}')

print("\n")

for key,value in favorite_languages.items():
	if value == "":
		print(f'Please {key}, type your favorite language: ', end ="")
		favorite_languages[key] = input()
	else:
		print(f'Thanks {key}, for responding!')


print(f"Elapsed time: {time.time() - start}")
#6-6. Polling: Use the code in favorite_languages.py (page 104).
#•	 Make a list of people who should take the favorite languages poll. Include
#some names that are already in the dictionary and some that are not.
#•	 Loop through the list of people who should take the poll. If they have
#already taken the poll, print a message thanking them for responding.
#If they have not yet taken the poll, print a message inviting them to take
#the poll