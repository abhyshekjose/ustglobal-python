words = ["apple", "banana", "orange", "grape", "umbrella", "ice"]
vowels = list(filter(lambda word: word[0].lower() in 'aeiou', words))
print(vowels)
