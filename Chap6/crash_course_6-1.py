from os import system
from random import randint
import time

system("cls")

start = time.time()

information = {}

information["First_name"] = "Ana"
information["Last_name"] = "Maria"
information["Age"] = "67"
information["City"] = "Santos Dumont"

for key,value in information.items():
	print(f"{key} is: {value}")

print(f"Elapsed time: {time.time() - start}")


# Dictionary methods: .keys(), .values() and .items()

#6-1. Person: Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each
#piece of information stored in your dictionary