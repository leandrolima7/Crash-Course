import time

start = time.time()

odd_1 = list(range(1,21,2))

print("First method")
for odd in odd_1:
	print(odd)

odd_2 = [odd for odd in range(1,21) if odd % 2 != 0]

print("\n")

print("Second method")
for odd in odd_2:
	print(odd)

print("\n")

if len(odd_1) == len(odd_2):
	if odd_1 == odd_2:
		print("The methods have generated identical lists!")
	else:
		print("The methods have generated different lists!")
else:
	print("The methods have generated different lists!\nSizes are different!")

print(f"Elapsed time {time.time() - start}")

