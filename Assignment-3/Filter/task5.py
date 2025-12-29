words = ["madam", "python", "level", "world", "radar"]
palindromes = list(filter(lambda word: word == word[::-1], words))
print(palindromes)
