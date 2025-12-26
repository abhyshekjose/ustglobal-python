# map() applies a function to every element in an iterable (like a list) and returns a map object.
numbers = [1,2,3,4,5,6]
print("Original Numbers:", numbers)
squared_numbers = map(lambda x: x**2, numbers)

print("Squared Numbers:", list(squared_numbers))