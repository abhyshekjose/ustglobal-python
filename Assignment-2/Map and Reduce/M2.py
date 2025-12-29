from functools import reduce
result = reduce(lambda x, y: x * y, [1, 2, 3, 4])

# reduce() keeps combining values until one result is left.
print(result)