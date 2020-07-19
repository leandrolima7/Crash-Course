from os import system
from random import randint
import time

system("cls")

start = time.time()

alien_color = "green"

print("Type your name: ", end = "")
name = input()

print(f"{name}, what is the alien's color? ")
print("Answer: ", end = "")
color = input()

if(color == "green"):
	print(f"You are right, {name}! The alien’s color is green! For that you've earned 5 point")
else:
	print(f"You are wrong, {name}! The alien’s color is not {color}! For that you've earned 10 point")

print(f"Elapsed time: {time.time() - start}s", end = "")