from os import system
from random import randint
import time

system("cls")

start = time.time();

username = ["admin","leandro","bob","admin","maria","vanessa","jonathan","ana"]

for name in username:
	if name == username[0]:
		print(f"Hello {username[0]},would you like to see a status report?")
	else:
		print(f"Hello {name}, thank you for logging in againw!")


print(f"Elapsed time: {time.time() - start}s")