from os import system
from random import randint
import time

start = time.time()

system("cls")

x = randint(0,2)

if x == 0:
    alien_color = "green"
elif x == 1:
    alien_color = "yellow"
elif x == 2:
    alien_color = "red"


print("Type your name: ", end = "")
name = input()

print(f"{name}, what is the alien's color? ")
print("Answer: ", end = "")
color = input()

if(color == "green"):
	print(f"You are right, {name}! The alien’s color is green! For that you've earned 5 point")
elif(color == "yellow"):
	print(f"You are right, {name}! The alien’s color is green! For that you've earned 10 point")
elif(color == "red"):
	print(f"You are right, {name}! The alien’s color is green! For that you've earned 15 point")
else:
	print(f"You are wrong, {name}! The alien’s color is not {color}! For that you've earned 10 point")

print(f"Elapsed time: {time.time() - start}s", end = "")

