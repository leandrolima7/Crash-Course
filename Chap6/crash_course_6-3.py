from os import system
from random import randint
import time

system("cls")

start = time.time() 

glossary = {"remove":"method used to remove items of from a list by using the valor of the item",
"pop":"is a method used to remove an item in a @list at @any position by including the index of the item you want to remove in parentheses",
"reverse":"is a method used to reverse the original order of a list"
}

for key,value in glossary.items():
	print(f"{key}: \n\t{value}\n")

print(f"\nElapsed time: {time.time() - start}")


#6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
#However, to avoid confusion, let’s call it a glossary.
#•	 Think of five programming words you’ve learned about in the previous
#chapters. Use these words as the keys in your glossary, and store their
#meanings as values.
#•	 Print each word and its meaning as neatly formatted output. You might
#print the word followed by a colon and then its meaning, or print the word
#on one line and then print its meaning indented on a second line. Use the
#newline character (\n) to insert a blank line between each word-meaning
#pair in your output.