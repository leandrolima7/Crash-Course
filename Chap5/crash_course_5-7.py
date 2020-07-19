from os import system
from random import randint
import time

start = time.time()

system("cls")

favorite_fruits = ["apple","papaya","banana","avocado","greap"]

print(f"Hello! My name is Leandro! I dare you to guess my one of my favorites fruits!")

print("My favorite fruit is: ", end = "")
aux = input()

if(aux == favorite_fruits[0]):
	print(f"Yeees, I really lobe Apple!")
elif(aux  == favorite_fruits[1]):
	print(f"I love eating Papaya!")
elif(aux  == favorite_fruits[1]):
	print(f"Bananas is one of my favorites!")
elif(aux  == favorite_fruits[1]):
	print(f"Yeees, I do love Avocados!")
elif(aux  == favorite_fruits[1]):
	print(f"I looooove it! You are right!")
else:
	print(f"Nooo, sorry! {aux} is not among my favorites!")


print(f"Elapsed time: {time.time() - start}s", end = "")

