sentence = "Python list comprehension makes code more readable"

long_words = [word for word in sentence.split() if len(word) > 4]

print(long_words)

