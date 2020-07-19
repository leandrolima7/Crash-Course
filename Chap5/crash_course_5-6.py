from os import system
from random import randint
import time

start = time.time()

system("cls")

age = randint(0,98)

print(f"Hello! My name is Leandro! I am {age} years old!")

if(age < 2):
	print(f"So, I am a baby!")
elif(age  >= 2 and age < 4):
	print(f"So, I am a toddler!")
elif(age  >= 4 and age < 13):
	print(f"So, I am a kid!")
elif(age  >= 13 and age < 20):
	print(f"So, I am a teenager!")
elif(age  >= 20 and age < 65):
	print(f"So, I am an adult!")
elif(age  >= 65):
	print(f"So, I am an elder!")


print(f"Elapsed time: {time.time() - start}s", end = "")

