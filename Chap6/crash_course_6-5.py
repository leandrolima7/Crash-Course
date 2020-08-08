from os import system
from random import randint
import time

system("cls")

start = time.time()

river = {"Amazonas":"Brazil","Nilo":"Egypt","Yangtze":"China"}

for key,value in river.items():
	print(f"The {key} river runs through {value}.")

print(f"Elapsed time: {time.time() - start}")
#6-5. Rivers: Make a dictionary containing three major rivers and the country
#each river runs through. One key-value pair might be 'nile': 'egypt'.
#•	 Use a loop to print a sentence about each river, such as The Nile runs
#through Egypt.
#•	 Use a loop to print the name of each river included in the dictionary.
#•	 Use a loop to print the name of each country included in the dictionary.