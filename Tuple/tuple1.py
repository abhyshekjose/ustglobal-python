t = (1, 2, 3, 4)
#Since tuples are immutable, you must convert it to a list, modify it, and convert it back.
temp = list(t)
temp[2] = 100
t = tuple(temp)

print(t)
