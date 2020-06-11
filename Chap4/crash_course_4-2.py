from os import system

animals = ["dogs","cats","birds"]

for each in animals:
	print(each)

print("\n")

for each in animals:
	if each == "dog":
		print(f"I love {each}")
	elif each == "cats":
		print(f"After long years, now i like {each}")
	else:
		print(f"{each} are meant to fly free")

print("\n")

print(f"I love {animals[0]}, {animals[1]} and {animals[2]}")