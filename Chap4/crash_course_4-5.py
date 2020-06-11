import time

lista = list(range(1,1000001))

print(f"Lista starts at {min(lista)} and ends at {max(lista)}")

start = time.time()

print(f"The sum all elements in Lista is: {sum(lista)}")

print(f"Elapsed time: {time.time() - start}")