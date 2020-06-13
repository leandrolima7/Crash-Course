import time

start = time.time()

lista = ["vasco","da","gama","a","sua","fama","assim","se","fez"]

print(f"The first three items in the list are: {lista[:3]}")

print(f"The items from the middle are: {lista[2:-2]}")

print(f"The last three items in the list are: {lista[-3:]}")

print(f"Elapsed time: {time.time() - start}")