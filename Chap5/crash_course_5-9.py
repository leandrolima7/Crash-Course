from os import system
from random import randint
import time

system("cls")

start = time.time();

select_mode = randint(0,1)

print(select_mode)

username = []

if select_mode == 0:
	username = ["admin","leandro","bob","admin","maria","vanessa","jonathan","ana"]
else:
	username = []

if username: #this if test checks if the list contains something
	for name in username:
		if name == username[0]:
			print(f"Hello {username[0]},would you like to see a status report?")
			username.remove(name)
		else:
			print(f"Hello {name}, thank you for logging in againw!")
			username.remove(name)
else:
	print(f"We need to find some users! The list is empty!")


print(f"Elapsed time: {time.time() - start}s")

# if list returns True if the list is not empty
#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
#not empty.
#•	 If the list is empty, print the message We need to find some users!
#•	 Remove all of the usernames from your list, and make sure the correct
#message is printed.