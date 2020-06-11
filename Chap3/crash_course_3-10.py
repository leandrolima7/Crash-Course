#creating an empty list
songs = [];

#adding an element
songs.append("Metropolis")


print(songs[0].title())

#appending
songs.append('The Odyssey')
print(songs[1].upper())

#insert
songs.insert(2,'Down From The Sky')
print(songs[2].lower())

#del
del songs[2]

print(songs)

#pop
poped = songs.pop()
print(songs)

songs.append("Inception of the End")

#pop
poped = songs.pop(1)
print(songs)

songs.append("Comming Home")
print(songs)

#Remove
songs.remove("Comming Home")
print(songs)

songs.append("What the Dead Man Say")
songs.append("Beed into me")
songs.append("This Loss")

#sorted()
print(sorted(songs))

print(sorted(songs,reverse=True))

#reverse()
print(songs)
songs.reverse()
print(songs)
songs.reverse()
print(sorted)

#sort()
songs.sort()
print(songs)
songs.sort(reverse=True)
print(songs)