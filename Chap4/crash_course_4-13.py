from os import system
import time
system('cls')
start = time.time()
buffet = ("rice","bean","chicken","spaghetti","carote")

while (time.time() - start) < 30:
	buffet = ("rice","bean","chicken","spaghetti","carote")

	print("Foods avaliable today:")

	for foods in buffet:
		print(foods)

	time.sleep(5)
	system('cls')
	#########################################################
	buffet = ("banana","bean","chicken","lasagn","carote")

	print("Foods avaliable tomorrow:")

	for foods in buffet:
		print(foods)
	time.sleep(5)
	system('cls')
	

print(f"Elapsed time: {time.time() - start}")



