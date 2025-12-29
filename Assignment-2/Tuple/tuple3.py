# List are Mutable
List = [1, 2, 4, 4, 3, 3, 3, 6, 5] # Modifying an element in the list `a`

List[3] = 77
print("Updated List:", List)


# Tuples are Immutable
b = (0, 1, 2, 3)

b[0] = 4 # Attempting to modify a tuple
print(b)