invite = ["Ana", "Vó","Nessa","Juh"]
msg =["Hello","would you like to have dinmer alongside me?","come to dinner with me","let us have dinner at my place today","let us have dinner togheter"]
print(f"{msg[0]} {invite[0]} {msg[1]}")
print(f"{msg[0]} {invite[3]} {msg[4]}")
print(f"{msg[0]} {invite[1]} {msg[3]}")
print(f"{msg[0]} {invite[2]} {msg[2]}")
msg1 = "Unfortunently,"
msg2 = "can't come"
print(f"{msg1} {invite[1]} {msg2}")
#the remove method removes only the first value from the list by the value .remove('value')
#wilhe .pop method removes by position str.pop(position)
invite.remove('Vó')
invite.insert(-1,'Pedro')
print(f"{msg[0]} {invite[0]} {msg[1]}")
print(f"{msg[0]} {invite[3]} {msg[4]}")
print(f"{msg[0]} {invite[1]} {msg[3]}")
print(f"{msg[0]} {invite[2]} {msg[2]}")
