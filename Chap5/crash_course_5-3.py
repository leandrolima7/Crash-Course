from os import system
from random import randint
import time

system("cls")

start = time.time()

alien_color = "blue"

print("Type your name: ", end = "")
name = input();

print(f"{name}, guess the Alien Color: ", end = "")
guess = input()

if(guess == alien_color):
	print(f"Congratulations, {name}! You've just won 5 points!\n")
else:
	print(f"{name}, wrong answer!\n")

print(f"Elapsed time: {time.time() - start}s",  end ="")