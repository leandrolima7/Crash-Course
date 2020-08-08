from os import system
from random import randint
import time

system("cls")

start = time.time()

favorite = {"Leandro":7,"Ana":5,"Jonathan":4,"Vanessa":9,"Vó":1}

for key,value in favorite.items():
	print(f"{key}'s favorite number is: {value}")

print(f"Elapsed time: {time.time() - start}")

#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
#Think of five names, and use them as keys in your dictionary. Think of a favorite
#number for each person, and store each as a value in your dictionary. Print
#each person’s name and their favorite number. For even more fun, poll a few
#friends and get some actual data for your program.