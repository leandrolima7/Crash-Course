#when we use str.sort(), str.reverse() it returns nothing, because they are void functions
places = ["Bora Bora","Santos Dumont","Norway","Dennamark","Holland"]

print(f"1 {places}\n")

#prints list in orde, but does not modifies it permanently
print(f"2 {sorted(places)}\n")

print(f"3 {places}\n")

print(f"4 {sorted(places,reverse=True)} \n")

print(f"5 {places}\n")

places.reverse()
print(f"6 {places}\n")

places.reverse()
print(f"7 {places}\n")

places.sort()
print(f"8 {places}\n")

#This order the list in reverse order, so from the bigger to the smaller
places.sort(reverse=True)
print(f"9 {places}\n")