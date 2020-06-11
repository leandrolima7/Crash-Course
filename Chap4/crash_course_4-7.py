import time

start = time.time()

multiples = [number for number in range(3,31) if number % 3 == 0]

for mult in multiples:
	print(mult)

multiples2 = []

for number in range(3,31):
	if number % 3 == 0:
		multiples2.append(number)

print("\n")
for mult in multiples2:
	print(mult)

if len(multiples) == len(multiples2):
	if multiples2 == multiples:
		print("Equal")
	else:
		print("Not equal")
else:
	print("Not equal")

print(f"\nElapsed time: {time.time() - start}")