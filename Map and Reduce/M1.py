# map() applies a function to every element in an iterable (like a list) and returns a map object.
numbers = [1,2,3,4,5,6,7,8,9,10]

squared_numbers = map(lambda x: x**2, numbers)

print("Squared Numbers:", list(squared_numbers))