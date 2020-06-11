import time

start = time.time()

cubes = [ pow(numb,3) for numb in range(1,11)]

for cubes in cubes:
	print(cubes)

print(f"Elapsed time {start - time.time()}")