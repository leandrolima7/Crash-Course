from os import system
from random import randint
import time

system("cls")

current_users = ["leandro","bob","maria","vanessa","jonathan","ana"]

new_users = ["lima","bob","vó","conceição","nascimento","maria"]

for user in new_users:
	aux = True
	for c_u in current_users:
		if user == c_u:
			print(f"The name {user} is not available! Enter a new username: ", end = "")
			new_users.append(input())
			new_users.remove(user)
			aux = False
			break
	if aux:
		print(f"The username {user} is available")
		aux = False

#5-10. Checking Usernames: Do the following to create a program that simulates
#how websites ensure that everyone has a unique username.
#•	 Make a list of five or more usernames called current_users.
#•	 Make another list of five usernames called new_users. Make sure one or
#two of the new usernames are also in the current_users list.
#•	 Loop through the new_users list to see if each new username has already
#been used. If it has, print a message that the person will need to enter a
#new username. If a username has not been used, print a message saying
#that the username is available.
#•	 Make sure your comparison is case insensitive. If 'John' has been used,
#'JOHN' should not be accepted.