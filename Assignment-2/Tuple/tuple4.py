t = (1, 2, 3, 4)

temp = list(t)
temp[2] = 100
t = tuple(temp)

print(t)
