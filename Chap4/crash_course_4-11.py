pizza = ["calabresa", "Catupiry", "Quatro Queijos"]

for kind in pizza:
	print(kind)

for kind in pizza:
	print(f"I Like {kind} pizza!")

print("I really love pizaa!")

#This copies the elements in the pizza to friends pizza
#if you do friends pizza = pizza, friends pizza points to pizza
#so the are not different list, but different way to access pizza
friend_pizza = pizza[:]

pizza.insert(1,"Frango")
pizza.append("Portuguesa")

print("\n")

friend_pizza.append("Chocolate")
friend_pizza.insert(3,"Carne seca")

print("My favorite pizzas are: ")

for pizza in pizza:
	print(pizza)

print("\n")

print("My friends' favorite pizzas are: ")

for pizzaf in friend_pizza:
	print(pizzaf)