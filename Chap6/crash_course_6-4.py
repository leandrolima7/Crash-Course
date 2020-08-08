from os import system
from random import randint
import time

system("cls")

start = time.time()


glossary = {"remove":"method used to remove items of from a list by using the valor of the item",
"pop":"is a method used to remove an item in a @list at @any position by including the index of the item you want to remove in parentheses",
"reverse":"is a method used to reverse the original order of a list",
"for":"is a method used to go through statructeres data"
}

for key in glossary.keys():
	print(f'Key: {key}')

print("\n")

for value in glossary.values():
	print(f"Value: {value}")

print("\n")

for key,value in glossary.items():
	print(f"{key}: is {value}")

print(f"Elapsed time: {time.time()-start}")
#6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
#up the code from Exercise 6-3 (page 102) by replacing your series of print
#statements with a loop that runs through the dictionary’s keys and values.
#When you’re sure that your loop works, add five more Python terms to your
#glossary. When you run your program again, these new words and meanings
#should automatically be included in the output.