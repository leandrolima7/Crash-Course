import time

start = time.time()

cubes = []

for i in range (1,11):
	cubes.append(i**3)

for i in cubes:
	print(i)

print(f"\nElapsed time {time.time() - start}")